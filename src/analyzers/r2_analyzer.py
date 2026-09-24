#!/usr/bin/env python3
import sys, json, r2pipe, subprocess
from pathlib import Path

def analyze_binary(binary_path: str, output_json: str):
    binary_path = Path(binary_path).resolve()
    if not binary_path.exists():
        print(f"[-] Файл не найден: {binary_path}")
        sys.exit(1)

    print(f"[*] Запуск Radare2 анализа для: {binary_path.name}")
    r2 = r2pipe.open(str(binary_path), flags=['-e', 'bin.relocs.apply=true'])
    r2.cmd('aaa')
    
    report = {
        "binary": binary_path.name,
        "arch": "x86_64" if r2.cmd('e asm.bits').strip() == "64" else "x86",
        "bits": r2.cmd('e asm.bits').strip(),
        "functions": [],
        "dangerous_calls": [],
        "interesting_strings": [],
        "gadgets": [],
        "safe_return_addresses": [],
        "rop_targets": {},
        "vulnerability_indicators": {}
    }

    # 1. Функции
    funcs = []
    try:
        funcs = json.loads(r2.cmd('aflj'))
        for f in funcs:
            name = f.get('name', '')
            if not name.startswith('fcn.') and not name.startswith('entry'):
                report["functions"].append({"name": name, "address": hex(f.get('addr', 0))})
    except: pass

    # Создаем единый список всех имен функций в нижнем регистре для надежного поиска
    all_func_names_lower = [f.get('name', '').lower() for f in funcs]

    # Безопасные адреса
    priority_names = ["main", "sym._exit", "exit", "sym.__libc_csu_fini"]
    for target_name in priority_names:
        for f in funcs:
            if f.get('name', '') == target_name:
                report["safe_return_addresses"].append({"name": f['name'], "address": hex(f.get('addr', 0))})
                break

    # 2. Опасные вызовы (ищем по именам функций, включая sym.imp.__isoc99_scanf и т.д.)
    dangerous_inputs = ['scanf', 'gets', 'strcpy', 'strcat', 'read', 'sprintf']
    dangerous_exec = ['system', 'execve', 'popen']
    
    malloc_count = sum(1 for name in all_func_names_lower if 'malloc' in name)
    has_dangerous_input = any(any(inp in name for name in all_func_names_lower) for inp in dangerous_inputs)
    has_dangerous_execution = any(any(exec_fn in name for name in all_func_names_lower) for exec_fn in dangerous_exec)

    # Заполняем dangerous_calls для отчета
    for f in funcs:
        name = f.get('name', '').lower()
        if any(d in name for d in dangerous_inputs + dangerous_exec + ['malloc', 'free']):
            report["dangerous_calls"].append({"caller": "global/import", "callee": f.get('name', ''), "address": hex(f.get('addr', 0))})
            if any(d in name for d in dangerous_exec):
                report["rop_targets"][f.get('name', '').replace('sym.imp.', '')] = hex(f.get('addr', 0))

    # 3. Строки
    strings_list = []
    try:
        strings_list = json.loads(r2.cmd('izj'))
        for s in strings_list:
            val = s.get('string', '')
            if any(kw in val for kw in ["%p", "%x", "%s", "%n", "/bin/sh", "flag", "cat ", "system", "Welcome", "Duckerz"]):
                report["interesting_strings"].append({"address": hex(s.get('vaddr', 0)), "value": val.strip()})
                if "/bin/sh" in val:
                    report["rop_targets"]["bin_sh"] = hex(s.get('vaddr', 0))
    except: pass

    has_address_leak = any('%p' in s.get('string', '') for s in strings_list)

    # 4. Гаджеты через ROPgadget
    print("[*] Ищу ROP-гаджеты через ROPgadget...")
    try:
        result = subprocess.run(['ROPgadget', '--binary', str(binary_path), '--nojop'], capture_output=True, text=True, timeout=10)
        for line in result.stdout.split('\n'):
            if ' : ' in line and any(g in line for g in ['pop rdi', 'pop rsi', 'pop rdx', 'pop rax', 'jmp rsi', 'jmp rdi', 'jmp rax', 'ret']):
                parts = line.split(' : ')
                if len(parts) == 2:
                    report["gadgets"].append({"address": parts[0].strip(), "instruction": parts[1].strip()})
        report["gadgets"] = report["gadgets"][:50]
        print(f"[+] Найдено {len(report['gadgets'])} гаджетов")
    except Exception as e:
        print(f"[!] Ошибка при поиске гаджетов: {e}")

    # ==========================================================
    # 5. УЛУЧШЕННЫЙ ДЕТЕКТОР УЯЗВИМОСТЕЙ
    # ==========================================================
    report["vulnerability_indicators"] = {
        "malloc_calls": malloc_count,
        "has_dangerous_input": has_dangerous_input,
        "has_dangerous_execution": has_dangerous_execution,
        "has_address_leak": has_address_leak,
        "risk_level": "LOW"
    }

    # Логика определения риска (теперь гораздо точнее!)
    if malloc_count >= 1 and has_dangerous_input and has_dangerous_execution:
        report["vulnerability_indicators"]["risk_level"] = "HIGH (Potential Heap/Stack Buffer Overflow -> Command Injection)"
    elif has_dangerous_input and not has_dangerous_execution:
        report["vulnerability_indicators"]["risk_level"] = "MEDIUM (Potential Buffer Overflow, check for ROP/Canary)"
    elif has_address_leak:
        report["vulnerability_indicators"]["risk_level"] = "MEDIUM (Information Leak detected, check for PIE bypass)"

    # ==========================================================

    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=4)
    r2.quit()
    print(f"[+] Анализ завершён. Отчёт: {output_json}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python3 r2_analyzer.py <binary> <output.json>")
        sys.exit(1)
    analyze_binary(sys.argv[1], sys.argv[2])

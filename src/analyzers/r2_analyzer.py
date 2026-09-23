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
        "rop_targets": {}
    }

    # 1. Функции
    try:
        funcs = json.loads(r2.cmd('aflj'))
        for f in funcs:
            name = f.get('name', '')
            if not name.startswith('fcn.') and not name.startswith('sym.imp.') and not name.startswith('entry'):
                report["functions"].append({"name": name, "address": hex(f.get('addr', 0))})
    except: pass

    # Безопасные адреса
    priority_names = ["main", "sym._exit", "exit", "sym.__libc_csu_fini"]
    for target_name in priority_names:
        for f in funcs:
            if f.get('name', '') == target_name:
                report["safe_return_addresses"].append({
                    "name": f['name'],
                    "address": hex(f.get('addr', 0))
                })
                break

    # 2. Опасные вызовы
    dangerous_funcs = ["read", "scanf", "gets", "strcpy", "strcat", "sprintf", "printf", "system", "execve"]
    try:
        imports = json.loads(r2.cmd('iij'))
        for imp in imports:
            name = imp.get('name', '')
            if name in dangerous_funcs:
                xrefs_str = r2.cmd(f'axtj @ sym.imp.{name}')
                if xrefs_str and xrefs_str.strip() != '[]':
                    for x in json.loads(xrefs_str):
                        func_info = r2.cmd(f'afij @ {x["from"]}')
                        func_name = "unknown"
                        if func_info and func_info.strip() != '[]':
                            try: func_name = json.loads(func_info)[0].get('name', 'unknown')
                            except: pass
                        report["dangerous_calls"].append({"caller": func_name, "callee": name, "address": hex(x["from"])})
                        
                        if name in ["system", "execve"]:
                            report["rop_targets"][name] = hex(imp.get('plt', 0))
    except: pass

    # 3. Строки
    try:
        strings = json.loads(r2.cmd('izj'))
        for s in strings:
            val = s.get('string', '')
            if any(kw in val for kw in ["%p", "%x", "%s", "%n", "/bin/sh", "flag", "cat ", "system", "Welcome", "Duckerz"]):
                report["interesting_strings"].append({"address": hex(s.get('vaddr', 0)), "value": val.strip()})
                
                if "/bin/sh" in val:
                    report["rop_targets"]["bin_sh"] = hex(s.get('vaddr', 0))
    except: pass

    # 4. Гаджеты через ROPgadget (надёжнее, чем /R в radare2)
    print("[*] Ищу ROP-гаджеты через ROPgadget...")
    try:
        result = subprocess.run(
            ['ROPgadget', '--binary', str(binary_path), '--nojop'],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        # Парсим вывод ROPgadget
        for line in result.stdout.split('\n'):
            if ' : ' in line and any(g in line for g in ['pop rdi', 'pop rsi', 'pop rdx', 'jmp rsi', 'jmp rdi', 'jmp rax', 'ret']):
                parts = line.split(' : ')
                if len(parts) == 2:
                    addr = parts[0].strip()
                    gadget = parts[1].strip()
                    report["gadgets"].append({
                        "address": addr,
                        "instruction": gadget
                    })
        
        # Ограничиваем до 50 гаджетов
        report["gadgets"] = report["gadgets"][:50]
        print(f"[+] Найдено {len(report['gadgets'])} гаджетов")
    except Exception as e:
        print(f"[!] Ошибка при поиске гаджетов: {e}")

    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=4)
    r2.quit()
    print(f"[+] Анализ завершён. Отчёт: {output_json}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python3 r2_analyzer.py <binary> <output.json>")
        sys.exit(1)
    analyze_binary(sys.argv[1], sys.argv[2])

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
        "vulnerability_indicators": {},
        "writable_addresses": {},
        "binary_protections": {}  # НОВОЕ: Защиты бинарника (SUID, PIE, Canary и т.д.)
    }

    funcs = []
    try:
        funcs = json.loads(r2.cmd('aflj'))
        for f in funcs:
            name = f.get('name', '')
            if not name.startswith('fcn.') and not name.startswith('entry'):
                report["functions"].append({"name": name, "address": hex(f.get('addr', 0))})
    except: pass

    all_func_names_lower = [f.get('name', '').lower() for f in funcs]

    priority_names = ["main", "sym._exit", "exit", "sym.__libc_csu_fini"]
    for target_name in priority_names:
        for f in funcs:
            if f.get('name', '') == target_name:
                report["safe_return_addresses"].append({"name": f['name'], "address": hex(f.get('addr', 0))})
                break

    # РАСШИРЕННЫЙ СПИСОК ОПАСНЫХ ФУНКЦИЙ
    dangerous_inputs = ['scanf', 'gets', 'strcpy', 'strcat', 'read', 'sprintf', 'fgets']
    dangerous_exec = ['system', 'execve', 'popen']
    fmtstr_funcs = ['printf', 'fprintf', 'vprintf', 'syslog']
    file_ops = ['open', 'openat', 'fopen', 'stat', 'lstat', 'access', 'chmod', 'chown', 'readlink']
    priv_esc = ['setuid', 'seteuid', 'setresuid', 'setgid', 'setegid', 'getuid', 'geteuid', 'getgid']

    malloc_count = sum(1 for name in all_func_names_lower if 'malloc' in name)
    has_dangerous_input = any(any(inp in name for name in all_func_names_lower) for inp in dangerous_inputs)
    has_dangerous_execution = any(any(exec_fn in name for name in all_func_names_lower) for exec_fn in dangerous_exec)
    has_fmtstr_func = any(any(fmt in name for name in all_func_names_lower) for fmt in fmtstr_funcs)
    has_file_ops = any(any(f_op in name for name in all_func_names_lower) for f_op in file_ops)
    has_priv_esc = any(any(priv in name for name in all_func_names_lower) for priv in priv_esc)

    # Специфичные функции для TOCTOU
    has_stat_check = any('stat' in name or 'access' in name for name in all_func_names_lower)
    has_uid_check = any('getuid' in name or 'geteuid' in name for name in all_func_names_lower)
    has_file_open = any('open' in name or 'fopen' in name for name in all_func_names_lower)

    # Собираем все опасные вызовы для отчета
    all_dangerous = dangerous_inputs + dangerous_exec + fmtstr_funcs + file_ops + priv_esc + ['malloc', 'free']
    for f in funcs:
        name = f.get('name', '').lower()
        if any(d in name for d in all_dangerous):
            report["dangerous_calls"].append({"caller": "global/import", "callee": f.get('name', ''), "address": hex(f.get('addr', 0))})
            if any(d in name for d in dangerous_exec):
                report["rop_targets"][f.get('name', '').replace('sym.imp.', '')] = hex(f.get('addr', 0))

    strings_list = []
    try:
        strings_list = json.loads(r2.cmd('izj'))
        for s in strings_list:
            val = s.get('string', '')
            if any(kw in val.lower() for kw in ["%p", "%x", "%s", "%n", "/bin/sh", "flag", ".txt", "root", "welcome", "duckerz", "target", "error", "permission", "don't own"]):
                report["interesting_strings"].append({"address": hex(s.get('vaddr', 0)), "value": val.strip()})
                if "/bin/sh" in val:
                    report["rop_targets"]["bin_sh"] = hex(s.get('vaddr', 0))
    except: pass

    has_address_leak = any('%p' in s.get('string', '') for s in strings_list)

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

    try:
        sections = json.loads(r2.cmd('iSj'))
        for sec in sections:
            if sec.get('name') in ['.bss', '.data'] and 'w' in sec.get('perm', '').lower():
                report["writable_addresses"][sec.get('name')] = hex(sec.get('vaddr', 0))
                break
    except: pass

    # ==========================================================
    # НОВОЕ: Анализ защит бинарника (SUID, PIE, Canary, NX, RELRO)
    # ==========================================================
    try:
        checksec_output = subprocess.run(['checksec', '--file', str(binary_path)], capture_output=True, text=True, timeout=5)
        checksec_text = checksec_output.stdout.lower()
        
        report["binary_protections"] = {
            "has_suid": "suid" in checksec_text or "setuid" in checksec_text,
            "has_pie": "pie" in checksec_text and "no pie" not in checksec_text,
            "has_canary": "canary" in checksec_text and "no canary" not in checksec_text,
            "has_nx": "nx" in checksec_text and "nx disabled" not in checksec_text,
            "has_relro": "relro" in checksec_text
        }
    except:
        report["binary_protections"] = {
            "has_suid": False,
            "has_pie": False,
            "has_canary": False,
            "has_nx": False,
            "has_relro": False
        }

    # ==========================================================
    # УЛУЧШЕННЫЙ ДЕТЕКТОР УЯЗВИМОСТЕЙ (Теперь с TOCTOU!)
    # ==========================================================
    report["vulnerability_indicators"] = {
        "malloc_calls": malloc_count,
        "has_dangerous_input": has_dangerous_input,
        "has_dangerous_execution": has_dangerous_execution,
        "has_fmtstr_func": has_fmtstr_func,
        "has_file_operations": has_file_ops,
        "has_privilege_escalation": has_priv_esc,
        "has_address_leak": has_address_leak,
        "has_stat_check": has_stat_check,
        "has_uid_check": has_uid_check,
        "has_file_open": has_file_open,
        "risk_level": "LOW"
    }

    # Логика определения риска (приоритет от высокого к низкому)
    if has_fmtstr_func and has_dangerous_input:
        report["vulnerability_indicators"]["risk_level"] = "HIGH (Potential Format String Vulnerability)"
    elif has_stat_check and has_uid_check and has_file_open:
        report["vulnerability_indicators"]["risk_level"] = "HIGH (Potential TOCTOU / Race Condition Vulnerability)"
    elif has_file_ops and (has_dangerous_input or has_priv_esc):
        report["vulnerability_indicators"]["risk_level"] = "HIGH (Potential File Logic / Symlink Vulnerability)"
    elif malloc_count >= 1 and has_dangerous_input:
        report["vulnerability_indicators"]["risk_level"] = "HIGH (Potential Heap/Stack Buffer Overflow)"
    elif has_dangerous_input and not has_dangerous_execution:
        report["vulnerability_indicators"]["risk_level"] = "MEDIUM (Potential Buffer Overflow, check for ROP/Canary)"
    elif has_address_leak:
        report["vulnerability_indicators"]["risk_level"] = "MEDIUM (Information Leak detected, check for PIE bypass)"

    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=4)
    r2.quit()
    print(f"[+] Анализ завершён. Отчёт: {output_json}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python3 r2_analyzer.py <binary> <output.json>")
        sys.exit(1)
    analyze_binary(sys.argv[1], sys.argv[2])

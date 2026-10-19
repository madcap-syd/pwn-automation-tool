#!/usr/bin/env python3
"""
Pwn Automation Framework v0.4
Автоматизация фаззинга, реверса и решения keygen-задач для pwn-челленджей
"""

import sys
from ghidra_analyzer import GhidraAnalyzer
from modules.asm_xor_solver import analyze_asm_xor
import os
import json

# Добавляем путь к модулям
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from modules.binary_analyzer import BinaryAnalyzer
from modules.offset_finder import OffsetFinder
from src.generators.exploit_generator import generate_exploit


def print_usage():
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║           PWN AUTOMATION FRAMEWORK v0.4                   ║
    ║     Автоматизация фаззинга, реверса и keygen              ║
    ╚═══════════════════════════════════════════════════════════╝
    
    Использование:
      python3 main.py analyze <binary>              - Полный анализ бинарника
      python3 main.py checksec <binary>             - Только защиты
      python3 main.py find-vuln <binary>            - Поиск уязвимых функций
      python3 main.py find-flag <binary>            - Поиск функции flag
      python3 main.py list-funcs <binary>           - Список всех функций
      python3 main.py analyze-func <binary> [func]  - Анализ конкретной функции
      python3 main.py find-offset <binary>          - Автопоиск смещения через cyclic + GDB
      python3 main.py calc-offset <binary> <buf> [align] - Ручной расчет смещения
      python3 main.py solve-keygen <binary>         - Автоматическое решение keygen через GDB
      python3 main.py ai-analyze <binary> [вопрос]  - ИИ-анализ бинарника через DeepSeek
      python3 main.py generate-exploit <binary>     - Автогенерация эксплойта (ROP, FSB, Heap Tcache)
      python3 main.py ghidra <binary> [опции]       - Глубокий анализ через Ghidra Headless
          --rust                                    - Режим для Rust/Go бинарников
          --timeout N                               - Таймаут анализа (по умолч. 120с)
          --report FILE                             - Сохранить отчет в Markdown
""")



def solve_keygen(binary_path):
    """Автоматическое решение keygenme через GDB"""
    from modules.keygen_gdb_solver import KeygenGDBSolver
    
    print("\n🔓 ЗАПУСК АВТОМАТИЧЕСКОГО РЕШЕНИЯ KEYGEN")
    print("=" * 60)
    
    solver = KeygenGDBSolver(binary_path)
    key = solver.solve()
    
    if key:
        print(f"\n[+] ✅ Флаг для отправки: {key}")
        print("[+] Не забудь закоммитить решение!")
    elif command == 'generate-exploit':
        print("\n🛠️ ЗАПУСК ГЕНЕРАТОРА ЭКСПЛОЙТОВ")
        print("=" * 60)
        try:
            # 1. Сначала запускаем полный анализ для создания JSON-отчета
            print("[*] Шаг 1: Анализ бинарника и создание отчета...")
            analyzer = BinaryAnalyzer(binary_path)
            analyzer.full_analysis()
            
            # Явно сохраняем отчет в JSON для генератора
            os.makedirs("output", exist_ok=True)
            
            # Универсальный сбор данных через getattr с дефолтными значениями
            report_data = {
                "binary": binary_path,
                "arch": getattr(analyzer, 'arch', 'x86_64'),
                "vulnerability_indicators": {
                    "risk_level": "HIGH" if getattr(analyzer, 'vuln_functions', []) else "MEDIUM",
                    "vulnerable_functions": getattr(analyzer, 'vuln_functions', []),
                    "has_dangerous_input": True
                },
                "gadgets": getattr(analyzer, 'gadgets', []),
                "rop_targets": getattr(analyzer, 'rop_targets', {}),
                "functions": {}
            }
            
            # Безопасно извлекаем функции из ELF
            elf = getattr(analyzer, 'elf', None)
            if elf and hasattr(elf, 'functions'):
                for name, func in elf.functions.items():
                    report_data["functions"][name] = {"address": hex(func.address)}
            
            # Безопасно извлекаем GOT/PLT
            report_data["got_entries"] = getattr(analyzer, 'got_entries', {})
            report_data["plt_entries"] = getattr(analyzer, 'plt_entries', {})
            
            with open("output/analysis.json", "w") as f:
                json.dump(report_data, f, indent=2)
            print("[+] Отчет сохранен в output/analysis.json")
            
            # 2. Генерируем эксплойт на основе созданного отчета
            print("[*] Шаг 2: Генерация эксплойта...")
            from src.generators.exploit_generator import generate_exploit
            
            json_report = "output/analysis.json"
            output_exploit = "exploit.py"
            
            generate_exploit(json_report, output_exploit)
            
            print(f"\n[+] ✅ Эксплойт успешно сгенерирован: {output_exploit}")
            print("[!] Проверь сгенерированный код и адаптируй OFFSET под задачу!")
            
        except FileNotFoundError:
            print("[-] ❌ Отчет output/analysis.json не найден.")
            print("[*] Попробуй вручную: python3 main.py analyze <binary>")
        except Exception as e:
            print(f"[-]  Ошибка генерации: {e}")

    else:
        print("\n[-] ❌ Автоматическое решение не сработало.")
        print("[*] Попробуй вручную через GDB:")
        print(f"    gdb {binary_path}")
        print(f"    (gdb) start")
        print(f"    (gdb) break *$rebase(0x141a)")
        print(f"    (gdb) continue")
        print(f"    (gdb) x/s $rbp-0x30")



def cmd_ghidra(args):
    """Обработчик команды ghidra для глубокого анализа бинарника."""
    try:
        analyzer = GhidraAnalyzer(args.binary, timeout=args.timeout, force_rust=args.rust)
        results = analyzer.analyze()
        if results:
            print("\n" + "="*80)
            print("КРАТКАЯ СВОДКА АНАЛИЗА GHIDRA")
            print("="*80)
            if results.get('functions'):
                for func in results['functions']:
                    print(f"🎯 {func['name']} @ {func['address']}")
                    print(f"   Ключи: {', '.join(func['keywords'])}")
            if args.report:
                analyzer.save_report(results, args.report)
            else:
                import json
                json_output = args.binary + "_ghidra_analysis.json"
                with open(json_output, 'w') as f:
                    json.dump(results, f, indent=2)
                print(f"\n💾 Результаты: {json_output}")
    except Exception as e:
        print(f"❌ Ошибка Ghidra анализа: {e}")
        import sys
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command in ['help', '-h', '--help']:
        print_usage()
        sys.exit(0)
    
    if len(sys.argv) < 3:
        print("❌ Укажи путь к бинарнику!")
        print_usage()
        sys.exit(1)
    
    binary_path = sys.argv[2]
    
    if not os.path.exists(binary_path):
        print(f"❌ Файл не найден: {binary_path}")
        sys.exit(1)
    
    # === КОМАНДА SOLVE-KEYGEN (не требует BinaryAnalyzer) ===
    if command == 'solve-keygen':
        solve_keygen(binary_path)
        return
    
    elf_commands = ['analyze', 'checksec', 'find-vuln', 'find-flag', 'list-funcs', 'analyze-func', 'find-offset', 'calc-offset', 'generate-exploit']
    if command in elf_commands:
        analyzer = BinaryAnalyzer(binary_path)
    else:
        analyzer = None
    
    # === КОМАНДЫ АНАЛИЗА ===
    if command == 'analyze':
        analyzer.full_analysis()
    
    elif command == 'checksec':
        analyzer.checksec()
    
    elif command == 'find-vuln':
        analyzer.find_vulnerable_functions()
    
    elif command == 'find-flag':
        analyzer.find_flag_function()
    
    elif command == 'list-funcs':
        print(f"\n📋 Список функций в {binary_path}:")
        print(f"{'='*60}")
        for name, func in analyzer.elf.functions.items():
            print(f"  {name:30s} {hex(func.address)}")
        print(f"{'='*60}\n")
    
    elif command == 'analyze-func':
        from modules.disassembler import Disassembler
        func_name = sys.argv[3] if len(sys.argv) > 3 else 'vuln'
        disasm = Disassembler(binary_path)
        disasm.full_function_analysis(func_name)
    
    elif command == 'find-offset':
        finder = OffsetFinder(binary_path)
        prompt = b'Input: ' 
        offset = finder.find_offset(prompt=prompt, max_size=200)
        
        if offset is None:
            print("⚠️ Автоматический поиск не сработал. Используй ручной расчет.")
            print("   Пример: python3 main.py calc-offset <binary> <размер_буфера> [выравнивание]")
    
    elif command == 'calc-offset':
        if len(sys.argv) < 4:
            print("❌ Укажи размер буфера!")
            print("   Пример: python3 main.py calc-offset vuln 100 0")
            sys.exit(1)
        
        buffer_size = int(sys.argv[3])
        alignment = int(sys.argv[4]) if len(sys.argv) > 4 else 0
        
        finder = OffsetFinder(binary_path)
        finder.calculate_from_ghidra(buffer_size, alignment)
    
    elif command == 'generate-exploit':
        print("\n🛠️ ЗАПУСК ГЕНЕРАТОРА ЭКСПЛОЙТОВ")
        print("=" * 60)
        try:
            # 1. Сначала запускаем полный анализ для создания JSON-отчета
            print("[*] Шаг 1: Анализ бинарника и создание отчета...")
            analyzer = BinaryAnalyzer(binary_path)
            analyzer.full_analysis()
            
            # Явно сохраняем отчет в JSON для генератора
            os.makedirs("output", exist_ok=True)
            
            # Универсальный сбор данных через getattr с дефолтными значениями
            report_data = {
                "binary": binary_path,
                "arch": getattr(analyzer, 'arch', 'x86_64'),
                "vulnerability_indicators": {
                    "risk_level": "HIGH" if getattr(analyzer, 'vuln_functions', []) else "MEDIUM",
                    "vulnerable_functions": getattr(analyzer, 'vuln_functions', []),
                    "has_dangerous_input": True
                },
                "gadgets": getattr(analyzer, 'gadgets', []),
                "rop_targets": getattr(analyzer, 'rop_targets', {}),
                "functions": {}
            }
            
            # Безопасно извлекаем функции из ELF
            elf = getattr(analyzer, 'elf', None)
            if elf and hasattr(elf, 'functions'):
                for name, func in elf.functions.items():
                    report_data["functions"][name] = {"address": hex(func.address)}
            
            # Безопасно извлекаем GOT/PLT
            report_data["got_entries"] = getattr(analyzer, 'got_entries', {})
            report_data["plt_entries"] = getattr(analyzer, 'plt_entries', {})
            
            with open("output/analysis.json", "w") as f:
                json.dump(report_data, f, indent=2)
            print("[+] Отчет сохранен в output/analysis.json")
            
            # 2. Генерируем эксплойт на основе созданного отчета
            print("[*] Шаг 2: Генерация эксплойта...")
            from src.generators.exploit_generator import generate_exploit
            
            json_report = "output/analysis.json"
            output_exploit = "exploit.py"
            
            generate_exploit(json_report, output_exploit)
            
            print(f"\n[+] ✅ Эксплойт успешно сгенерирован: {output_exploit}")
            print("[!] Проверь сгенерированный код и адаптируй OFFSET под задачу!")
            
        except FileNotFoundError:
            print("[-] ❌ Отчет output/analysis.json не найден.")
            print("[*] Попробуй вручную: python3 main.py analyze <binary>")
        except Exception as e:
            print(f"[-]  Ошибка генерации: {e}")

    elif command == 'ai-analyze':
        print("\nИИ-АНАЛИЗ (DeepSeek)")
        print("=" * 60)
        from modules.ai_analyzer import analyze_binary
        custom_q = " ".join(sys.argv[3:]) if len(sys.argv) > 3 else ""
        result = analyze_binary(binary_path, custom_q)
        print(result)


    elif command == 'ghidra':
        print("\n🦑 GHIDRA HEADLESS АНАЛИЗ")
        print("=" * 60)
        try:
            is_rust = '--rust' in sys.argv
            timeout = 120
            report_file = None
            # Парсим дополнительные аргументы
            i = 3
            while i < len(sys.argv):
                if sys.argv[i] == '--rust':
                    is_rust = True
                elif sys.argv[i] == '--timeout' and i + 1 < len(sys.argv):
                    timeout = int(sys.argv[i + 1])
                    i += 1
                elif sys.argv[i] == '--report' and i + 1 < len(sys.argv):
                    report_file = sys.argv[i + 1]
                    i += 1
                i += 1
            
            analyzer = GhidraAnalyzer(binary_path, timeout=timeout, force_rust=is_rust)
            results = analyzer.analyze()
            if results:
                print("\n" + "="*80)
                print("КРАТКАЯ СВОДКА АНАЛИЗА GHIDRA")
                print("="*80)
                if results.get('functions'):
                    print(f"\n🎯 Найдено {len(results['functions'])} ключевых функций:")
                    for func in results['functions']:
                        print(f"   - {func['name']} @ {func['address']}")
                        print(f"     Ключи: {', '.join(func['keywords'])}")
                if report_file:
                    analyzer.save_report(results, report_file)
                else:
                    import json
                    json_output = binary_path + "_ghidra_analysis.json"
                    with open(json_output, 'w') as f:
                        json.dump(results, f, indent=2)
                    print(f"\n💾 Результаты: {json_output}")
        except Exception as e:
            print(f"❌ Ошибка Ghidra анализа: {e}")
            import traceback
            traceback.print_exc()


    elif command == 'solve-asm-xor':
        print("\n🧩 АВТОМАТИЧЕСКИЙ ПОИСК И РЕШЕНИЕ XOR-ПАТТЕРНОВ В АССЕМБЛЕРЕ")
        print("=" * 60)
        analyze_asm_xor(binary_path)

    else:
        print(f"❌ Неизвестная команда: {command}")
        print_usage()
        sys.exit(1)


if __name__ == '__main__':
    main()

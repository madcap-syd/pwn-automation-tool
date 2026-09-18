#!/usr/bin/env python3
"""
Pwn Automation Framework v0.3
Автоматизация фаззинга и реверса для pwn-челленджей
"""

import sys
import os

# Добавляем путь к модулям
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from modules.binary_analyzer import BinaryAnalyzer
from modules.offset_finder import OffsetFinder


def print_usage():
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║           🐇 PWN AUTOMATION FRAMEWORK v0.3             ║
    ║      Автоматизация фаззинга и реверса для pwn            ║
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
    """)


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
    
    analyzer = BinaryAnalyzer(binary_path)
    
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
        # Стандартный промпт для picoCTF. Если задача другая, можно будет добавить аргумент
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
    
    else:
        print(f"❌ Неизвестная команда: {command}")
        print_usage()
        sys.exit(1)


if __name__ == '__main__':
    main()

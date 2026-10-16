#!/usr/bin/env python3
"""Тестовый скрипт для GhidraAnalyzer."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ghidra_analyzer import GhidraAnalyzer

def test_analyzer(binary_path, is_rust=False):
    print(f" Тестирование: {binary_path}")
    print("="*80)
    
    try:
        timeout = 600 if is_rust else 120
        analyzer = GhidraAnalyzer(binary_path, timeout=timeout, force_rust=is_rust)
        
        print(f"✅ Ghidra: {analyzer.ghidra_path}")
        print(f"✅ Тип бинарника: {analyzer.binary_type}")
        print(f"✅ Таймаут: {analyzer.timeout} сек\n")
        
        results = analyzer.analyze()
        
        if results:
            print("\n" + "="*80)
            print("РЕЗУЛЬТАТЫ")
            print("="*80)
            
            if results.get('functions'):
                for func in results['functions']:
                    print(f"\n🎯 {func['name']} @ {func['address']}")
                    print(f"   Ключи: {', '.join(func['keywords'])}")
                    print(f"   Код:\n{func['code'][:400]}...\n")
            
            # Сохраняем отчет
            report_path = binary_path + "_report.md"
            analyzer.save_report(results, report_path)
            return True
        else:
            print("\n❌ Анализ не дал результатов")
            return False
            
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python3 test_ghidra_analyzer.py <binary> [--rust]")
        sys.exit(1)
    
    binary_path = sys.argv[1]
    is_rust = "--rust" in sys.argv
    success = test_analyzer(binary_path, is_rust)
    sys.exit(0 if success else 1)

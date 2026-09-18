"""
Disassembler - автоматический анализ ассемблерного кода
"""

import subprocess
import re
from typing import Dict, List, Optional
from modules.stack_analyzer import StackAnalyzer


class Disassembler:
    """Анализ дизассемблированного кода"""
    
    def __init__(self, binary_path: str):
        self.binary_path = binary_path
        self.disasm = self._get_disassembly()
    
    def _get_disassembly(self) -> str:
        """Получает полный дизассемблер бинарника"""
        result = subprocess.run(
            ['objdump', '-d', self.binary_path],
            capture_output=True,
            text=True
        )
        return result.stdout
    
    def find_function_disasm(self, func_name: str) -> Optional[str]:
        """Найти дизассемблер конкретной функции"""
        pattern = f'<{func_name}>:'
        lines = self.disasm.split('\n')
        
        func_lines = []
        in_function = False
        
        for line in lines:
            if pattern in line:
                in_function = True
                func_lines.append(line)
            elif in_function:
                if line.strip() == '' or (not line.startswith(' ') and '<' in line and ':' in line):
                    break
                func_lines.append(line)
        
        return '\n'.join(func_lines) if func_lines else None
    
    def find_vulnerable_calls(self, func_name: str) -> List[Dict]:
        """Находит вызовы опасных функций"""
        func_disasm = self.find_function_disasm(func_name)
        if not func_disasm:
            return []
        
        dangerous = ['gets@plt', 'strcpy@plt', 'sprintf@plt', 'scanf@plt', 'printf@plt', 'system@plt']
        results = []
        
        for line in func_disasm.split('\n'):
            for func in dangerous:
                if func in line:
                    addr_match = re.search(r'^\s*([0-9a-f]+):', line)
                    if addr_match:
                        addr = int(addr_match.group(1), 16)
                        results.append({
                            'function': func,
                            'address': addr,
                            'instruction': line.strip()
                        })
        
        return results
    
    def full_function_analysis(self, func_name: str):
        """Полный анализ функции"""
        print(f"\n🔬 ПОЛНЫЙ АНАЛИЗ ФУНКЦИИ: {func_name}")
        print(f"{'='*60}")
        
        # 1. Анализ структуры стека
        stack_analyzer = StackAnalyzer(self)
        stack_info = stack_analyzer.analyze_function_stack(func_name)
        
        # 2. Уязвимые вызовы
        vuln_calls = self.find_vulnerable_calls(func_name)
        if vuln_calls:
            print(f"\n⚠️  Уязвимые вызовы:")
            for call in vuln_calls:
                print(f"   {call['function']} по адресу {hex(call['address'])}")
        else:
            print(f"\n✅ Явных уязвимых вызовов не найдено")
        
        # 3. Подсказки
        if stack_info:
            stack_analyzer.print_exploit_hints(stack_info)
        
        print(f"{'='*60}\n")
        
        return {
            'stack_info': stack_info,
            'vulnerable_calls': vuln_calls
        }


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        disasm = Disassembler(sys.argv[1])
        func_name = sys.argv[2] if len(sys.argv) > 2 else 'vuln'
        disasm.full_function_analysis(func_name)
    else:
        print("Использование: python3 disassembler.py <binary> [function_name]")

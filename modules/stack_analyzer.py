"""
StackAnalyzer - автоматический анализ структуры стека функции
Определяет размер буфера, смещение до адреса возврата и т.д.
"""

import re
from typing import Dict, Optional


class StackAnalyzer:
    """Анализ структуры стека функции"""
    
    def __init__(self, disassembler):
        self.disasm = disassembler
    
    def analyze_function_stack(self, func_name: str) -> Optional[Dict]:
        """
        Анализирует структуру стека функции через дизассемблер.
        
        Возвращает:
        - stack_allocation: сколько байт выделено на стеке
        - buffer_offset: смещение буфера от RBP/EBP
        - saved_bp_size: размер сохраненного EBP/RBP (4 или 8)
        - return_address_offset: смещение до адреса возврата
        """
        func_disasm = self.disasm.find_function_disasm(func_name)
        if not func_disasm:
            return None
        
        print(f"\n🔍 Анализ структуры стека функции '{func_name}':")
        print(f"{'='*60}")
        
        # Определяем архитектуру (32 или 64 бит)
        is_64bit = '%rsp' in func_disasm or '%rdi' in func_disasm
        saved_bp_size = 8 if is_64bit else 4
        bp_reg = 'rbp' if is_64bit else 'ebp'
        sp_reg = 'rsp' if is_64bit else 'esp'
        
        print(f"   Архитектура: {'64-бит' if is_64bit else '32-бит'}")
        print(f"   Размер сохраненного {bp_reg.upper()}: {saved_bp_size} байт")
        
        # Ищем 'sub $0xXXX,%rsp' - общее выделение стека
        sub_pattern = rf'sub\s+\$(0x[0-9a-f]+),%{sp_reg}'
        sub_matches = re.findall(sub_pattern, func_disasm, re.IGNORECASE)
        
        stack_alloc = 0
        if sub_matches:
            stack_alloc = int(sub_matches[0], 16)
            print(f"   Выделено на стеке: {stack_alloc} байт (0x{stack_alloc:x})")
        else:
            print(f"   ⚠️  Не найдено явное выделение стека через sub")
        
        # Ищем 'lea -0xXXX(%rbp),%rax' (64-бит) или 'lea -0xXXX(%ebp),%eax' (32-бит)
        # ВАЖНО: для 32-бит регистры начинаются с 'e' (eax, ebx...), для 64-бит с 'r' (rax, rbx...)
        if is_64bit:
            lea_pattern = rf'lea\s+-0x([0-9a-f]+)\(%{bp_reg}\),%r[abcd]x'
        else:
            lea_pattern = rf'lea\s+-0x([0-9a-f]+)\(%{bp_reg}\),%e[abcd]x'
        
        lea_matches = re.findall(lea_pattern, func_disasm, re.IGNORECASE)
        
        if lea_matches:
            # Берем самое большое смещение (обычно это основной буфер)
            buffer_offset = max(int(m, 16) for m in lea_matches)
            print(f"   Смещение буфера от {bp_reg.upper()}: {buffer_offset} байт")
            
            return {
                'stack_allocation': stack_alloc,
                'buffer_offset_from_bp': buffer_offset,
                'saved_bp_size': saved_bp_size,
                'return_address_offset': buffer_offset + saved_bp_size,
                'is_64bit': is_64bit
            }
        
        print(f"   ⚠️  Не найдено lea инструкции для буфера")
        return None
    
    def print_exploit_hints(self, analysis: Dict):
        """Выводит подсказки для эксплойта на основе анализа стека"""
        if not analysis:
            return
        
        print(f"\n💡 Подсказки для эксплойта:")
        print(f"{'='*60}")
        
        offset = analysis['return_address_offset']
        bp_name = 'RBP' if analysis['is_64bit'] else 'EBP'
        
        print(f"   Смещение до адреса возврата: {offset} байт")
        print(f"   Формула: {analysis['buffer_offset_from_bp']} (буфер) + {analysis['saved_bp_size']} ({bp_name}) = {offset}")
        
        if analysis['is_64bit']:
            print(f"   ⚠️  64-бит: аргументы передаются через регистры (rdi, rsi, rdx...)")
        else:
            print(f"   ℹ️  32-бит: аргументы передаются через стек")
        
        print(f"{'='*60}\n")

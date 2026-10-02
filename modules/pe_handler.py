"""
Модуль для обработки Windows PE-файлов в pwntools.
Решает проблему "Magic number does not match" при работе с .exe файлами.
"""
import os
from pwn import context

def is_pe_file(binary_path):
    """Проверяет, является ли файл Windows PE-бинарником."""
    if not os.path.exists(binary_path):
        return False
    
    # Проверяем расширение
    if binary_path.lower().endswith('.exe') or binary_path.lower().endswith('.dll'):
        return True
    
    # Проверяем PE-сигнатуру в заголовке (MZ)
    try:
        with open(binary_path, 'rb') as f:
            magic = f.read(2)
            return magic == b'MZ'
    except Exception:
        return False

def setup_pe_context(binary_path, arch=None):
    """
    Настраивает контекст pwntools для PE-файла.
    ВАЖНО: НЕ устанавливает context.binary, чтобы избежать ошибки парсинга ELF.
    """
    if not is_pe_file(binary_path):
        return False
    
    # Определяем архитектуру из PE-заголовка
    if arch is None:
        try:
            with open(binary_path, 'rb') as f:
                f.seek(0x3C)  # Смещение PE-заголовка
                pe_offset = int.from_bytes(f.read(4), 'little')
                f.seek(pe_offset + 4)  # Machine field
                machine = int.from_bytes(f.read(2), 'little')
                
                if machine == 0x14C:  # IMAGE_FILE_MACHINE_I386
                    arch = 'i386'
                elif machine == 0x8664:  # IMAGE_FILE_MACHINE_AMD64
                    arch = 'amd64'
                else:
                    arch = 'i386'  # По умолчанию 32-бит
        except Exception:
            arch = 'i386'
    
    context.arch = arch
    context.os = 'windows'
    context.endian = 'little'
    
    print(f"[*] PE-файл обнаружен: {binary_path}")
    print(f"[*] Архитектура: {arch}")
    print(f"[*] ОС: windows")
    print(f"[!] context.binary НЕ установлен (избегаем ошибки парсинга ELF)")
    
    return True

def get_pe_arch(binary_path):
    """Возвращает архитектуру PE-файла ('i386' или 'amd64')."""
    try:
        with open(binary_path, 'rb') as f:
            f.seek(0x3C)
            pe_offset = int.from_bytes(f.read(4), 'little')
            f.seek(pe_offset + 4)
            machine = int.from_bytes(f.read(2), 'little')
            
            if machine == 0x8664:
                return 'amd64'
            return 'i386'
    except Exception:
        return 'i386'

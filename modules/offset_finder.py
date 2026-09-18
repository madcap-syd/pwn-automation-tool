"""
OffsetFinder v0.2 - автоматический поиск смещения до адреса возврата (EIP/RIP)
Использует cyclic pattern (паттерн Де Брёйна) и GDB для перехвата краша.
Исправлено: права доступа, рабочая директория, безопасная передача паттерна.
"""

from pwn import context, process, cyclic, cyclic_find, log
import subprocess
import re
import os
import stat
import tempfile


class OffsetFinder:
    def __init__(self, binary_path):
        self.binary_path = os.path.abspath(binary_path)
        context.binary = self.binary_path
        
    def _ensure_executable(self):
        """Проверяет и добавляет права на выполнение, если нужно"""
        file_stat = os.stat(self.binary_path)
        if not (file_stat.st_mode & stat.S_IXUSR):
            log.info(f"Файл не исполняемый. Добавляем права +x...")
            os.chmod(self.binary_path, file_stat.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
            log.success(f"Права на выполнение добавлены!")

    def _ensure_flag_file(self, binary_dir):
        """Создает фейковый flag.txt, если его нет (нужно для некоторых CTF)"""
        flag_path = os.path.join(binary_dir, 'flag.txt')
        if not os.path.exists(flag_path):
            log.info(f"Файл flag.txt не найден. Создаем фейковый флаг...")
            with open(flag_path, 'w') as f:
                f.write("FAKE_FLAG{test123}\n")

    def find_offset(self, prompt=b'', max_size=200):
        """
        Автоматически находит смещение до перезаписи EIP/RIP.
        """
        # 1. Подготовка
        self._ensure_executable()
        binary_dir = os.path.dirname(self.binary_path)
        self._ensure_flag_file(binary_dir)
        
        if context.arch == 'i386':
            reg = 'eip'
        else:
            reg = 'rip'
            
        log.info(f"Генерация cyclic pattern размером {max_size} байт...")
        pattern = cyclic(max_size)
        
        # Записываем паттерн во временный файл (безопаснее, чем echo)
        with tempfile.NamedTemporaryFile(delete=False, suffix='.txt', mode='wb') as tmp:
            tmp.write(pattern)
            tmp_path = tmp.name
            
        log.info(f"Запуск бинарника через GDB для перехвата краша (регистр: {reg})...")
        
        try:
            # Запускаем GDB в batch-режиме из директории бинарника
            result = subprocess.run(
                ['gdb', '-batch', 
                 '-ex', f'run < {tmp_path}', 
                 '-ex', f'info registers {reg}', 
                 '-ex', 'quit', 
                 self.binary_path],
                capture_output=True,
                text=True,
                cwd=binary_dir # ВАЖНО: запускаем из папки с бинарником!
            )
            
            # Удаляем временный файл
            os.unlink(tmp_path)
            
            output = result.stdout + result.stderr
            
            # Ищем значение регистра в выводе GDB
            # Пример вывода GDB: eip 0x6161616c 0x6161616c
            match = re.search(rf'{reg}\s+0x([0-9a-fA-F]+)', output, re.IGNORECASE)
            
            if match:
                crash_value = match.group(1)
                crash_int = int(crash_value, 16)
                
                offset = cyclic_find(crash_int)
                
                if offset != -1:
                    log.success(f"Краш по адресу: 0x{crash_value}")
                    log.success(f"🎯 Найдено смещение до адреса возврата: {offset} байт!")
                    return offset
                else:
                    log.warning(f"Значение 0x{crash_value} не найдено в cyclic pattern.")
                    return None
            else:
                log.warning("Не удалось перехватить значение регистра из GDB.")
                log.info("Возможно, программа не упала или GDB не запустился.")
                return None
                
        except Exception as e:
            log.error(f"Ошибка при поиске смещения: {e}")
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
            return None

    def calculate_from_ghidra(self, buffer_size, alignment=0):
        """Ручной расчет на основе данных из Ghidra/дизассемблера."""
        saved_bp_size = 4 if context.arch == 'i386' else 8
        offset = buffer_size + alignment + saved_bp_size
        
        log.info(f"Расчет смещения (Ghidra):")
        log.info(f"  Размер буфера: {buffer_size}")
        log.info(f"  Выравнивание: {alignment}")
        log.info(f"  Сохраненный EBP/RBP: {saved_bp_size}")
        log.success(f"  ИТОГО смещение: {offset} байт")
        
        return offset

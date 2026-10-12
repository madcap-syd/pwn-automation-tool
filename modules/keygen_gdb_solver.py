#!/usr/bin/env python3
"""
Модуль автоматического решения Keygen-задач через GDB (обход PIE)
Использует $rebase() для установки брейкпоинтов в PIE-бинарниках.
"""

import subprocess
import os
import re
import tempfile

class KeygenGDBSolver:
    def __init__(self, binary_path, break_offset=0x141a, key_addr_offset="-0x30", input_length=36):
        """
        binary_path: путь к бинарнику
        break_offset: смещение в бинарнике, где ключ уже собран (до проверки длины)
        key_addr_offset: смещение от RBP, где лежит собранный ключ (например, "-0x30")
        input_length: длина правильного ключа (для ввода заглушки)
        """
        self.binary = os.path.abspath(binary_path)
        self.break_offset = break_offset
        self.key_addr_offset = key_addr_offset
        self.input_length = input_length
        
    def solve(self):
        print(f"[*] Запуск автоматического решения для {self.binary}")
        print(f"[*] Брейкпоинт на смещении: {hex(self.break_offset)}")
        print(f"[*] Чтение ключа по адресу: RBP{self.key_addr_offset}")
        
        # Создаем временный GDB-скрипт
        gdb_script = f"""
set pagination off
set confirm off
set environment LINES 24
start
break *$rebase({hex(self.break_offset)})
continue
echo INPUT_NEEDED\\n
"""
        
        # Запускаем GDB в интерактивном режиме через pexpect-подобный подход
        # Но для простоты используем subprocess с pty
        import pty
        import select
        
        master, slave = pty.openpty()
        
        proc = subprocess.Popen(
            ['gdb', '-q', '-x', '/dev/stdin', self.binary],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            bufsize=0
        )
        
        # Отправляем скрипт
        proc.stdin.write(gdb_script.encode())
        proc.stdin.flush()
        
        # Читаем вывод до момента ввода
        output = b""
        while b"INPUT_NEEDED" not in output:
            try:
                chunk = proc.stdout.read(1)
                output += chunk
            except:
                break
        
        print("[*] Программа остановлена на брейкпоинте. Вводим заглушку...")
        
        # Вводим заглушку нужной длины
        dummy_input = b"A" * self.input_length + b"\n"
        proc.stdin.write(dummy_input)
        proc.stdin.flush()
        
        # Читаем вывод после ввода
        output = b""
        import time
        time.sleep(1)
        
        # Пытаемся прочитать ключ через команду GDB
        gdb_cmd = f"x/s $rbp{self.key_addr_offset}\nquit\n"
        proc.stdin.write(gdb_cmd.encode())
        proc.stdin.flush()
        
        # Собираем весь оставшийся вывод
        remaining = b""
        try:
            while True:
                chunk = proc.stdout.read(1)
                if not chunk:
                    break
                remaining += chunk
        except:
            pass
        
        full_output = output + remaining
        
        # Ищем ключ в выводе
        # Формат: 0x7fffffffdb00:\t"academy{...}"
        match = re.search(rb'"(academy\{[^}]+\})"', full_output)
        if match:
            key = match.group(1).decode('utf-8')
            print(f"[+] НАЙДЕН КЛЮЧ: {key}")
            return key
        else:
            print("[-] Не удалось извлечь ключ из вывода GDB")
            print("[*] Полный вывод GDB:")
            print(full_output.decode('utf-8', errors='ignore'))
            return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Использование: python3 keygen_gdb_solver.py <binary> [break_offset]")
        sys.exit(1)
    
    binary = sys.argv[1]
    offset = int(sys.argv[2], 16) if len(sys.argv) > 2 else 0x141a
    
    solver = KeygenGDBSolver(binary, break_offset=offset)
    solver.solve()

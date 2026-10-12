#!/usr/bin/env python3
"""
Автоматическое решение Keygenme через динамический анализ (GDB)
Модуль для pwn-automation-tool
"""

from pwn import *
import gdb

context.binary = './keygenme'
context.log_level = 'info'

# Адрес после сборки финального ключа (перед проверкой длины)
BREAKPOINT_ADDR = 0x141a  # mov rax, qword [var_d8h]

def solve():
    print("[*] Запуск keygenme в GDB...")
    
    # Создаем GDB скрипт
    gdb_script = f"""
    set pagination off
    set confirm off
    break *{BREAKPOINT_ADDR}
    run
    # Читаем финальный ключ из памяти (36 байт по адресу rbp-0x30)
    x/36s $rbp-0x30
    # Или читаем как строку
    printf "Key: %s\\n", (char*)($rbp-0x30)
    continue
    """
    
    with open('/tmp/gdb_solve.txt', 'w') as f:
        f.write(gdb_script)
    
    # Запускаем GDB
    gdb_cmd = f"gdb -q -x /tmp/gdb_solve.txt ./keygenme"
    result = process(gdb_cmd.split(), stdin=PTY)
    
    # Вводим тестовый ключ (36 символов)
    result.sendline(b"A" * 36)
    result.interactive()

if __name__ == '__main__':
    solve()

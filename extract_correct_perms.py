#!/usr/bin/env python3
import struct

with open('checkpass', 'rb') as f:
    # S-box таблицы (4 штуки по 256 байт)
    f.seek(0x8470)
    sbox0 = f.read(256)
    f.seek(0x8570)
    sbox1 = f.read(256)
    f.seek(0x8670)
    sbox2 = f.read(256)
    f.seek(0x8770)
    sbox3 = f.read(256)
    
    # Массивы перестановок (32 элемента по 8 байт = 256 байт каждый)
    # Round 0 starts at 0x9fb0
    # Round 1 starts at 0x9fb0 + 0x100 = 0xa0b0
    # Round 2 starts at 0xa1b0
    # Round 3 starts at 0xa2b0
    
    perms = []
    for i in range(4):
        offset = 0x9fb0 + (i * 0x100)
        f.seek(offset)
        # Читаем 32 64-битных значения (little-endian)
        perm_bytes = f.read(256)
        perm = list(struct.unpack('<32Q', perm_bytes))
        perms.append(perm)
        
        # Проверяем, является ли это валидной перестановкой (все числа 0-31)
        is_valid = sorted(perm) == list(range(32))
        print(f"Permutation {i} (offset 0x{offset:x}):")
        print(f"  Valid: {is_valid}")
        print(f"  Values: {perm}\n")


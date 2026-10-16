#!/usr/bin/env python3
import struct

# 1. Читаем S-box таблицы
with open('checkpass', 'rb') as f:
    f.seek(0x8470)
    sbox0 = f.read(256)
    f.seek(0x8570)
    sbox1 = f.read(256)
    f.seek(0x8670)
    sbox2 = f.read(256)
    f.seek(0x8770)
    sbox3 = f.read(256)

sboxes = [sbox0, sbox1, sbox2, sbox3]

# 2. Читаем массивы перестановок
perms = [
    [11, 4, 19, 13, 9, 29, 24, 28, 12, 20, 16, 25, 15, 0, 10, 5, 26, 1, 14, 6, 30, 3, 8, 27, 2, 31, 21, 17, 22, 18, 23, 7],
    [28, 16, 31, 8, 27, 26, 0, 17, 25, 21, 9, 2, 18, 24, 7, 22, 30, 11, 10, 23, 20, 19, 5, 4, 13, 12, 1, 3, 14, 15, 29, 6],
    [7, 2, 18, 11, 17, 5, 24, 0, 31, 19, 1, 3, 29, 14, 30, 22, 27, 21, 4, 16, 28, 10, 12, 25, 13, 8, 20, 6, 9, 23, 15, 26],
    [18, 13, 20, 5, 12, 29, 23, 0, 15, 9, 2, 1, 4, 6, 8, 24, 11, 22, 16, 10, 28, 14, 17, 21, 30, 27, 26, 25, 19, 7, 3, 31]
]

# 3. Читаем целевой массив
with open('checkpass', 'rb') as f:
    f.seek(0x9f70)
    target = list(f.read(32))

print("Target:", bytes(target).hex())

# 4. Строим обратные S-box
inv_sboxes = []
for sbox in sboxes:
    inv = [0] * 256
    for i in range(256):
        inv[sbox[i]] = i
    inv_sboxes.append(inv)

# 5. Строим обратные перестановки
inv_perms = []
for perm in perms:
    inv = [0] * 32
    for i in range(32):
        inv[perm[i]] = i
    inv_perms.append(inv)

# 6. Расшифровываем (от раунда 3 к 0)
result = target[:]
for round_idx in range(3, -1, -1):
    # Обратная перестановка
    temp = [0] * 32
    for i in range(32):
        temp[i] = result[inv_perms[round_idx][i]]
    result = temp
    
    # Обратный S-box
    for i in range(32):
        result[i] = inv_sboxes[round_idx][result[i]]

# 7. Выводим результат
flag_inner = bytes(result).decode('ascii', errors='replace')
print("\n🔓 ВНУТРЕННЯЯ ЧАСТЬ ФЛАГА:", flag_inner)
print("🔓 HEX:", bytes(result).hex())

# 8. Проверяем первый байт
first_byte = result[0]
print(f"\n🔍 Первый байт: 0x{first_byte:02x} ({chr(first_byte) if 32 <= first_byte < 127 else '?'})")

if first_byte < 0xc0:
    print("✅ Проверка < 0xC0 пройдена!")
else:
    print(" Проверка < 0xC0 НЕ пройдена!")

# 9. Формируем варианты
print("\n🚩 ВАРИАНТЫ ДЛЯ ОТПРАВКИ:")
print(f"1. academy{{{flag_inner}}}")
print(f"2. picoCTF{{{flag_inner}}}")
print(f"3. {flag_inner}")

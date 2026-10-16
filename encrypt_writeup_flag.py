#!/usr/bin/env python3

# Читаем S-box таблицы
with open('checkpass', 'rb') as f:
    f.seek(0x8470)
    t0 = f.read(256)
    f.seek(0x8570)
    t1 = f.read(256)
    f.seek(0x8670)
    t2 = f.read(256)
    f.seek(0x8770)
    t3 = f.read(256)

tables = [t0, t1, t2, t3]

# Флаг из райтапа (внутренняя часть)
writeup_flag = b"t1mingS1deChann3l_gVQSfJxl3VPFGQ"
print(f"Шифруем строку из райтапа: {writeup_flag.decode()}")
print(f"Длина: {len(writeup_flag)}")

# Применяем 4 раунда S-box (in-place, как мы видели в GDB)
encrypted = bytearray(writeup_flag)
for t in tables:
    for i in range(len(encrypted)):
        encrypted[i] = t[encrypted[i]]

print(f"\nРезультат шифрования (hex): {encrypted.hex()}")

# Наш целевой массив из GDB
target_hex = "1f9950d7b8223acbcf12aecbd9209948057b7b22cd0d46f9cfe6120105cbf97b"
print(f"Целевой массив из GDB  (hex): {target_hex}")

if encrypted.hex() == target_hex:
    print("\n✅ СОВПАДЕНИЕ! Флаг из райтапа ДЕЙСТВИТЕЛЬНО подходит к этим S-box!")
    print("Значит, проблема в том, что мы не прошли проверку '0xbf', или формат флага другой.")
else:
    print("\n❌ НЕ СОВПАДАЕТ. Значит, в этой версии бинарника:")
    print("1. Либо другие S-box (но GDB подтвердил наши!)")
    print("2. Либо есть перестановка байт, которую мы не учли.")
    print("3. Либо целевой массив в этом бинарнике ДРУГОЙ.")

# Давайте найдем ВСЕ 32-байтные последовательности в бинарнике и проверим, 
# является ли какая-то из них зашифрованным флагом из райтапа.
print("\n🔍 Поиск зашифрованного флага из райтапа в бинарнике...")
with open('checkpass', 'rb') as f:
    data = f.read()

idx = data.find(encrypted)
if idx != -1:
    print(f"✅ НАЙДЕНО! Зашифрованный флаг лежит в бинарнике по смещению: 0x{idx:x}")
else:
    print("❌ Зашифрованный флаг из райтапа НЕ найден в бинарнике.")
    print("Это означает, что авторы изменили либо S-box, либо целевой массив, либо и то, и другое.")

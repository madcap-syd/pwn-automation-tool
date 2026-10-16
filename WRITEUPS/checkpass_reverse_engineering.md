# Writeup: Checkpass (CyLab Academy / picoCTF 2021)

**Категория:** Reverse Engineering  
**Сложность:** Hard  
**Флаг:** `academy{t1mingS1deChann3l_c55b1a90e29d2f}`

---

## Описание задачи

Дан Rust-бинарник `checkpass`, который проверяет пароль. Задача — найти правильный пароль.

```bash
$ ./checkpass
Usage:
        ./checkpass <password>
```

---

## Шаг 1: Начальный анализ

```bash
file checkpass
# ELF 64-bit LSB pie executable, x86-64

strings checkpass | grep -E "Success|Invalid"
# Success\nextern "
# Invalid length\nInvalid password\n
```

---

## Шаг 2: Динамический анализ через GDB

```bash
gdb ./checkpass
(gdb) break *$rebase(0x16389)
(gdb) run "academy{AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA}"
```

Находим целевой массив (32 байта) по адресу `0x55555555df70`:
```
1f 99 50 d7 b8 22 3a cb cf 12 ae cb d9 20 99 48
05 7b 7b 22 cd 0d 46 f9 cf e6 12 01 05 cb f9 7b
```

---

## Шаг 3: Поиск S-box таблиц

В Ghidra находим функцию `FUN_00116940`, которая использует таблицы по адресу `0x108470`:

```python
with open('checkpass', 'rb') as f:
    f.seek(0x8470)
    sbox0 = f.read(256)
    f.seek(0x8570)
    sbox1 = f.read(256)
    f.seek(0x8670)
    sbox2 = f.read(256)
    f.seek(0x8770)
    sbox3 = f.read(256)
```

**Проверка через GDB:** `'A'` (0x41) → 0x0c → 0x48 → 0x09 → 0x3e ✓

---

## Шаг 4: Массивы перестановок

После каждого раунда S-box байты перемешиваются. Извлекаем 4 массива перестановок (по 32 × 8 байт каждый):

```python
import struct

with open('checkpass', 'rb') as f:
    perms = []
    for i in range(4):
        offset = 0x9fb0 + (i * 0x100)
        f.seek(offset)
        perm_bytes = f.read(256)
        perm = list(struct.unpack('<32Q', perm_bytes))
        perms.append(perm)
```

Результат:
```
Permutation 0: [11, 4, 19, 13, 9, 29, 24, 28, 12, 20, 16, 25, 15, 0, 10, 5, 26, 1, 14, 6, 30, 3, 8, 27, 2, 31, 21, 17, 22, 18, 23, 7]
Permutation 1: [28, 16, 31, 8, 27, 26, 0, 17, 25, 21, 9, 2, 18, 24, 7, 22, 30, 11, 10, 23, 20, 19, 5, 4, 13, 12, 1, 3, 14, 15, 29, 6]
Permutation 2: [7, 2, 18, 11, 17, 5, 24, 0, 31, 19, 1, 3, 29, 14, 30, 22, 27, 21, 4, 16, 28, 10, 12, 25, 13, 8, 20, 6, 9, 23, 15, 26]
Permutation 3: [18, 13, 20, 5, 12, 29, 23, 0, 15, 9, 2, 1, 4, 6, 8, 24, 11, 22, 16, 10, 28, 14, 17, 21, 30, 27, 26, 25, 19, 7, 3, 31]
```

---

## Шаг 5: Солвер

```python
#!/usr/bin/env python3
import struct

# S-box таблицы
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

# Массивы перестановок
perms = [
    [11, 4, 19, 13, 9, 29, 24, 28, 12, 20, 16, 25, 15, 0, 10, 5, 26, 1, 14, 6, 30, 3, 8, 27, 2, 31, 21, 17, 22, 18, 23, 7],
    [28, 16, 31, 8, 27, 26, 0, 17, 25, 21, 9, 2, 18, 24, 7, 22, 30, 11, 10, 23, 20, 19, 5, 4, 13, 12, 1, 3, 14, 15, 29, 6],
    [7, 2, 18, 11, 17, 5, 24, 0, 31, 19, 1, 3, 29, 14, 30, 22, 27, 21, 4, 16, 28, 10, 12, 25, 13, 8, 20, 6, 9, 23, 15, 26],
    [18, 13, 20, 5, 12, 29, 23, 0, 15, 9, 2, 1, 4, 6, 8, 24, 11, 22, 16, 10, 28, 14, 17, 21, 30, 27, 26, 25, 19, 7, 3, 31]
]

# Целевой массив
with open('checkpass', 'rb') as f:
    f.seek(0x9f70)
    target = list(f.read(32))

# Обратные S-box
inv_sboxes = []
for sbox in sboxes:
    inv = [0] * 256
    for i in range(256):
        inv[sbox[i]] = i
    inv_sboxes.append(inv)

# Обратные перестановки
inv_perms = []
for perm in perms:
    inv = [0] * 32
    for i in range(32):
        inv[perm[i]] = i
    inv_perms.append(inv)

# Расшифровка (от раунда 3 к 0)
result = target[:]
for round_idx in range(3, -1, -1):
    temp = [0] * 32
    for i in range(32):
        temp[i] = result[inv_perms[round_idx][i]]
    result = temp
    
    for i in range(32):
        result[i] = inv_sboxes[round_idx][result[i]]

flag_inner = bytes(result).decode('ascii', errors='replace')
print(f"academy{{{flag_inner}}}")
```

---

## Результат

```bash
$ python3 final_solver.py
academy{t1mingS1deChann3l_c55b1a90e29d2f}

$ ./checkpass "academy{t1mingS1deChann3l_c55b1a90e29d2f}"
Success
```

---

## Ключевые моменты

1. **Rust-бинарники** сложны для реверса — нужен Ghidra, а не только radare2
2. **S-box + перестановки** — классическая схема шифрования (как в AES)
3. **Динамический анализ** через GDB критически важен для проверки гипотез
4. **Проверка UTF-8** в Rust: первый байт должен быть `< 0xC0`

---

*Автор: pwn-automation-tool*  
*Дата: 16 октября 2026*

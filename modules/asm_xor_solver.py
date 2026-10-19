#!/usr/bin/env python3
"""
Модуль для автоматического обнаружения и решения XOR-паттернов в ассемблерных файлах (.S)
"""
import re
import os
import sys
from collections import Counter

def analyze_asm_xor(filepath):
    if not filepath.endswith('.S') and not filepath.endswith('.s'):
        print("[-] Этот модуль оптимизирован для исходных файлов ассемблера (.S / .s)")
        print("[*] Для бинарных файлов используйте radare2/ghidra анализ.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"[*] Анализируем: {filepath}")
    
    # Умный паттерн: ищет блок из двух movabsq и двух последующих movq
    block_pattern = re.compile(
        r'movabsq\s+\$(-?\d+),\s+%r[a-z]+\s*\n\s*'
        r'movabsq\s+\$(-?\d+),\s+%r[a-z]+\s*\n\s*'
        r'movq\s+%r[a-z]+,\s+(-?\d+)\(%rbp\)\s*\n\s*'
        r'movq\s+%r[a-z]+,\s+(-?\d+)\(%rbp\)'
    )
    
    matches = block_pattern.findall(content)
    
    if not matches:
        print("[-] Не найдено паттернов загрузки 64-битных констант (movabsq + movq).")
        return

    print(f"[+] Найдено {len(matches) * 2} загрузок констант в {len(matches)} блоках.")
    
    # Собираем все значения с их смещениями
    all_values = []
    for val1, val2, off1, off2 in matches:
        all_values.append((int(off1), int(val1)))
        all_values.append((int(off2), int(val2)))
    
    # Сортируем по смещениям (от меньшего к большему, т.е. от -144 к -32)
    all_values.sort(key=lambda x: x[0])
    
    print(f"[*] Найдены смещения: {[v[0] for v in all_values]}")
    
    # Группируем смежные смещения в массивы (разница 8 байт = одно 64-битное значение)
    arrays = []
    current_array = [all_values[0][1]]
    current_offset = all_values[0][0]
    
    for i in range(1, len(all_values)):
        offset, value = all_values[i]
        if offset == current_offset + 8:  # Смежное смещение
            current_array.append(value)
            current_offset = offset
        else:  # Разрыв — начинаем новый массив
            if len(current_array) >= 4:  # Только массивы из 4+ элементов
                arrays.append(current_array)
            current_array = [value]
            current_offset = offset
    
    # Добавляем последний массив
    if len(current_array) >= 4:
        arrays.append(current_array)
    
    if len(arrays) < 2:
        print(f"[-] Не удалось найти два массива. Найдено массивов: {len(arrays)}")
        return

    array1, array2 = arrays[0], arrays[1]
    
    print(f"[+] Обнаружен Массив 1: {len(array1)} элементов")
    print(f"[+] Обнаружен Массив 2: {len(array2)} элементов")

    # Ищем константу XOR в цикле
    xor_const_pattern = re.compile(r'xorl\s+\$(\d+),\s+%e[a-d]x')
    xor_matches = xor_const_pattern.findall(content)
    
    xor_const = 0
    if xor_matches:
        xor_const = int(Counter(xor_matches).most_common(1)[0][0])
        print(f"[+] Обнаружена константа XOR: {xor_const}")
    else:
        print("[!] Константа XOR не найдена, предполагаем 0")

    # Генерируем солвер
    print("\n" + "="*80)
    print("✅ XOR-ПАТТЕРН УСПЕШНО РАСПОЗНАН!")
    print("="*80)
    
    solver_code = f"""#!/usr/bin/env python3
# Авто-солвер для {os.path.basename(filepath)}
# Сгенерировано Pwn Automation Framework

def solve():
    array1_values = {array1}
    array2_values = {array2}
    xor_const = {xor_const}
    
    array1 = b''
    array2 = b''
    
    for val in array1_values:
        if val < 0:
            val = val & 0xFFFFFFFFFFFFFFFF
        array1 += val.to_bytes(8, 'little')
        
    for val in array2_values:
        if val < 0:
            val = val & 0xFFFFFFFFFFFFFFFF
        array2 += val.to_bytes(8, 'little')
        
    length = array1.index(b'\\x00') if b'\\x00' in array1 else len(array1)
    
    flag = b''
    for i in range(length):
        byte = (array1[i] ^ array2[i]) ^ i ^ xor_const
        flag += bytes([byte])
        
    try:
        print("\\n🏆 ФЛАГ:", flag.decode('ascii'))
    except:
        print("\\n ФЛАГ (bytes):", flag)

if __name__ == "__main__":
    solve()
"""
    
    output_solver = filepath.replace('.S', '_solver.py').replace('.s', '_solver.py')
    with open(output_solver, 'w', encoding='utf-8') as f:
        f.write(solver_code)
        
    print(f"💾 Солвер сохранен в: {output_solver}")
    print("\n🚀 Запускаем сгенерированный солвер:")
    print("-" * 80)
    
    exec(solver_code)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python3 modules/asm_xor_solver.py <file.S>")
        sys.exit(1)
    analyze_asm_xor(sys.argv[1])

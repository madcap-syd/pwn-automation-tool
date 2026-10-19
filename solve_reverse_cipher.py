#!/usr/bin/env python3
"""
Солвер для задачи reverse_cipher (picoCTF 2019 / Academy)
Обращает алгоритм шифрования из бинарника rev
"""

def main():
    # Зашифрованный флаг из файла rev_this
    cipher_text = b"academy{w1{1wq8c7_h4846}"
    
    print(f"[*] Зашифрованный текст: {cipher_text.decode('ascii')}")
    print(f"[*] Длина: {len(cipher_text)} байт")
    
    flag = bytearray(len(cipher_text))
    
    for i in range(len(cipher_text)):
        if i < 8:
            # Первые 8 байт копируются без изменений
            flag[i] = cipher_text[i]
        elif i == len(cipher_text) - 1:
            # Последний байт копируется без изменений
            flag[i] = cipher_text[i]
        else:
            # Байты 8..22
            if i % 2 == 0:
                # Четный индекс: cipher = plain + 5  =>  plain = cipher - 5
                flag[i] = (cipher_text[i] - 5) % 256
            else:
                # Нечетный индекс: cipher = plain - 2  =>  plain = cipher + 2
                flag[i] = (cipher_text[i] + 2) % 256
                
    result = flag.decode('ascii')
    
    print("\n" + "="*80)
    print("✅ ФЛАГ УСПЕШНО РАСШИФРОВАН!")
    print("="*80)
    print(f"\n{result}\n")
    print("="*80)

if __name__ == "__main__":
    main()

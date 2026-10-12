#!/usr/bin/env python3
from pwn import *

context.log_level = 'info'
HOST = 'xebec.cylabacademy.net'
PORT = 36043

try:
    print(f"Подключаемся к {HOST}:{PORT}...")
    io = remote(HOST, PORT)
    print("Подключено! Ждем приветственное сообщение (5 секунд)...")
    
    # Просто читаем всё, что придет за 5 секунд, ничего не отправляя
    banner = io.recv(timeout=5)
    
    print("\n" + "="*70)
    print("👀 ТОЧНЫЙ ТЕКСТ, КОТОРЫЙ ПРИСЛАЛ СЕРВЕР (в формате repr):")
    print("="*70)
    print(repr(banner))
    print("="*70 + "\n")
    
    # Также покажем это в обычном виде, чтобы было понятно
    print("В обычном виде:")
    print(banner.decode('utf-8', errors='ignore'))
    print("="*70 + "\n")
    
    io.close()
except Exception as e:
    print(f"Ошибка: {e}")

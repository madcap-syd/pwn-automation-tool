#!/usr/bin/env python3
"""
Клиент для Pwn Automation API
Отправляет бинарник на анализ и красиво выводит результаты.
"""

import requests
import argparse
import sys
import json
import re

# Адрес нашего API (в Docker)
API_URL = "http://localhost:8000"

def analyze_binary(filepath):
    print(f"[*] Отправка файла '{filepath}' на анализ...")
    
    try:
        with open(filepath, 'rb') as f:
            files = {'file': (filepath, f, 'application/octet-stream')}
            response = requests.post(f"{API_URL}/analyze", files=files, timeout=60)
            
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "success":
                print("\n" + "="*70)
                print("🎯 РЕЗУЛЬТАТЫ АНАЛИЗА")
                print("="*70)
                
                # Печатаем основной вывод нашего инструмента
                print(data["analysis_output"])
                
                # Если есть ошибки (например, предупреждение curses), покажем их внизу
                if data.get("errors"):
                    print("\n⚠️  ПРЕДУПРЕЖДЕНИЯ СИСТЕМЫ:")
                    print(data["errors"])
                    
                print("="*70)
                print("✅ Анализ успешно завершен!")
            else:
                print(f"❌ Ошибка API: {data}")
        else:
            print(f"❌ HTTP Ошибка: {response.status_code} - {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Не удалось подключиться к API. Убедитесь, что Docker-контейнер запущен!")
        print("   Команда для запуска: docker run -d -p 8000:8000 --name pwn-container pwn-api")
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")

def find_offset(filepath):
    print(f"[*] Поиск смещения для '{filepath}' через API...")
    
    try:
        with open(filepath, 'rb') as f:
            files = {'file': (filepath, f, 'application/octet-stream')}
            response = requests.post(f"{API_URL}/find-offset", files=files, timeout=60)
            
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "success":
                print("\n" + "="*70)
                print("📏 РЕЗУЛЬТАТЫ ПОИСКА СМЕЩЕНИЯ")
                print("="*70)
                
                # Выводим сырой вывод
                print(data["raw_output"])
                
                # Если API смог распарсить смещение, выделим его жирным
                if "parsed_offset" in data and data["parsed_offset"]:
                    print(f"\n🎯 ИТОГОВОЕ СМЕЩЕНИЕ (OFFSET): {data['parsed_offset']} БАЙТ")
                else:
                    print("\n⚠️  Не удалось автоматически определить смещение. Проверьте логи выше.")
                    
                print("="*70)
            else:
                print(f"❌ Ошибка API: {data}")
        else:
            print(f"❌ HTTP Ошибка: {response.status_code} - {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Не удалось подключиться к API. Запустите контейнер!")
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Клиент для Pwn Automation API")
    parser.add_argument("action", choices=["analyze", "offset"], help="Действие: analyze (полный анализ) или offset (поиск смещения)")
    parser.add_argument("file", help="Путь к анализируемому бинарному файлу")
    
    args = parser.parse_args()
    
    if args.action == "analyze":
        analyze_binary(args.file)
    elif args.action == "offset":
        find_offset(args.file)

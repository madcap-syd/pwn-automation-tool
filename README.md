# 🐇 Pwn Automation Framework

Автоматизированный инструмент для анализа бинарных файлов и поиска уязвимостей (Buffer Overflow, Format String), разработанный для CTF и обучения информационной безопасности.

## 🚀 Возможности
- **Анализ защит**: Автоматический checksec (PIE, Canary, NX, RELRO).
- **Поиск уязвимостей**: Сканирование на опасные функции (`gets`, `printf`, `strcpy`).
- **Auto Offset Finder**: Автоматический расчет смещения до EIP/RIP с помощью GDB и cyclic pattern.
- **Stack Analyzer**: Анализ структуры стека функции через дизассемблер.

## 📦 Установка и запуск (Docker)

Самый простой способ запустить инструмент на любой ОС (Windows, macOS, Linux):

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/ТВОЙ_НИК/pwn-automation-tool.git
   cd pwn-automation-tool
2. Соберите Docker-образ:
      docker build -t pwn-auto .
3. Запустите анализ (пример):
      docker run --rm -v $(pwd):/app pwn-auto analyze ./target_binary
   docker run --rm -v $(pwd):/app pwn-auto find-offset ./target_binary
(Флаг -v $(pwd):/app подключает твою текущую папку внутрь контейнера, чтобы инструмент видел твои файлы).

🛠 Локальный запуск (без Docker)

pip install -r requirements.txt
python3 main.py analyze <binary>



# Запускаем наш инструмент ВНУТРИ контейнера, передавая ему текущую папку
docker run --rm -v $(pwd):/app pwn-auto analyze ./ret2win
docker run --rm -v $(pwd):/app pwn-auto find-offset ./ret2win



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


---

### 🌐 ШАГ 4: Инициализация Git и отправка на GitHub

1. Зайди на [github.com](https://github.com/) и создай **новый пустой репозиторий** с именем `pwn-automation-tool`. Не добавляй туда README или `.gitignore`, создай его полностью пустым.
2. Скопируй URL созданного репозитория (например: `https://github.com/твой-ник/pwn-automation-tool.git`).

Выполни в терминале:
```bash
cd ~/pwn-automation-tool

# Инициализируем git
git init
git add .
git commit -m "Initial commit: Pwn Automation Framework v1.0"

# Привязываем к твоему репозиторию (ЗАМЕНИ URL НА СВОЙ!)
git branch -M main
git remote add origin https://github.com/ТВОЙ_НИК/pwn-automation-tool.git

# Отправляем код на GitHub
git push -u origin main

🏆 ШАГ 5: Проверка портативности (Магия Docker)

Теперь проверим, что инструмент работает изолированно и переносимо.
Убедись, что у тебя установлен Docker (в Kali он обычно есть, или sudo apt install docker.io).

# 1. Собираем образ (это создаст переносимую "коробку" с твоим инструментом)
docker build -t pwn-auto .

# 2. Тестируем! (Скачаем тестовый бинарник прямо в папку и прогоним через Docker)
wget https://ropemporium.com/binary/ret2win.zip
unzip ret2win.zip
chmod +x ret2win

# Запускаем наш инструмент ВНУТРИ контейнера, передавая ему текущую папку
docker run --rm -v $(pwd):/app pwn-auto analyze ./ret2win
docker run --rm -v $(pwd):/app pwn-auto find-offset ./ret2win



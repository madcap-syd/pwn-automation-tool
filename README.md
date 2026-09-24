# 🐇 Pwn Automation Framework

Автоматизированный инструмент для анализа бинарных файлов, поиска уязвимостей (Buffer Overflow, Format String) и обхода защит (Canary Leak). Разработан для CTF-соревнований и обучения информационной безопасности.

## 🚀 Возможности
- ⚡ **Молниеносный анализ:** Интеграция Radare2 (headless) + ROPgadget для сверхбыстрого извлечения гаджетов, строк и функций.
- 🧠 **Умная генерация эксплойтов:** Автопостроение ROP-цепочек (pop rdi, stack alignment) и ret2win через Jinja2-шаблоны на основе JSON-отчета.
- 🛡️ **Анализ защит:** Автоматический checksec (PIE, Canary, NX, RELRO, Stripped).
- 🔍 **Поиск уязвимостей:** Сканирование PLT/GOT на опасные функции (gets, printf, strcpy, system).
- 📏 **Auto Offset Finder:** Автоматический расчет смещения до EIP/RIP с помощью cyclic pattern и GDB.
- 📝 **Format String Analyzer:** Автопоиск смещения пользовательского ввода в стеке для эксплуатации уязвимостей форматной строки.
- 🛡️ **Canary Bypass Analyzer:** Точный GDB-анализ структуры стека функции для математически выверенного обхода Stack Canary.
- 🌐 **REST API & Python Client:** Возможность запуска анализа удаленно через API или удобный CLI-клиент.



## 📦 Установка и запуск (Docker)

Самый простой и надежный способ запустить инструмент на любой ОС (Windows, macOS, Linux), так как все зависимости (pwntools, gdb, radare2) уже включены в образ.

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/madcap-syd/pwn-automation-tool.git
   cd pwn-automation-tool


2. Соберите Docker-образ:

   
   ```bash
   docker build -t pwn-auto .
      # Полный анализ бинарника
   docker run --rm -v $(pwd):/app pwn-auto analyze ./target_binary
   
   # Автоматический поиск смещения BOF
   docker run --rm -v $(pwd):/app pwn-auto find-offset ./target_binary
   
   # Анализ стека для обхода Canary
   docker run --rm -v $(pwd):/app pwn-auto bypass-canary ./target_binary

   💡 Флаг -v $(pwd):/app подключает твою текущую папку внутрь контейнера, чтобы инструмент видел твои файлы.

## 🛠 Локальный запуск (без Docker)

Требует установленной ОС Linux (рекомендуется Kali Linux), Python 3.8+ и GDB/Radare2.

1. Установите зависимости:
   ```bash
      python3 -m venv venv
      source venv/bin/activate
      pip3 install -r requirements.txt

2. Запустите инструмент:
   ```bash
   python3 main.py analyze ./target_binary
   python3 main.py help  # Показать все доступные команды

## 🌐 Использование API и Клиента

Фреймворк включает в себя FastAPI сервер и Python-клиент для автоматизации в пайплайнах.

1. Запустите API сервер:
   ```bash
   python3 api_server.py

2. Используйте клиент для удаленного анализа:
   ```bash
   python3 client.py analyze http://localhost:8000 ./target_binary

## 📂 Структура проекта
```

pwn-automation-tool/
├── main.py                 # Точка входа CLI
├── api_server.py           # FastAPI сервер
├── client.py               # Python клиент для API
├── src/                    # Новые модули автоматизации
│   ├── analyzers/
│   │   └── r2_analyzer.py       # Анализ через Radare2 + ROPgadget
│   └── generators/
│       └── exploit_generator.py # Генератор эксплойтов (Jinja2)
├── modules/
│   ├── binary_analyzer.py  # Анализ защит и функций
│   ├── offset_finder.py    # Поиск смещения BOF (cyclic + GDB)
│   ├── fmtstr_analyzer.py  # Поиск смещения Format String
│   └── canary_analyzer.py  # GDB-анализ стека для обхода Canary
├── output/                 # Директория для JSON-отчетов и артефактов
├── Dockerfile              # Конфигурация Docker-образа
└── requirements.txt        # Зависимости Python
```

## 🤝 Вклад в проект

Pull Requests приветствуются! Для серьезных изменений, пожалуйста, сначала откройте Issue, чтобы обсудить, что вы хотите изменить.

## 📜 Лицензия

Этот проект распространяется под лицензией MIT. Используйте ответственно и только в образовательных целях или на легальных CTF-площадках.

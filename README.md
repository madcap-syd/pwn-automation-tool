# 🐇 Pwn Automation Framework

Автоматизированный инструмент для анализа бинарных файлов, поиска уязвимостей (Buffer Overflow, Format String) и обхода защит (Canary Leak, PIE). Разработан для CTF-соревнований и обучения информационной безопасности.

## 🚀 Возможности

-  **Молниеносный анализ:** Интеграция Radare2 (headless) + ROPgadget для сверхбыстрого извлечения гаджетов, строк и функций.
-  **Глубокий анализ через Ghidra Headless:** Автоматическое определение типа бинарника (C/C++, Rust, Go). Надежные Java-скрипты для 100% совместимости, извлечение декомпилированного кода ключевых функций и генерация Markdown-отчетов.
- 🧠 **Умный детектор уязвимостей (SAST):** Автоматически анализирует паттерны кода (например, malloc + scanf + system) и классифицирует уровень риска (LOW/MEDIUM/HIGH), предлагая вектор атаки.
- 🔗 **Автогенерация эксплойтов:** Умное построение ROP-цепочек (pop rdi, stack alignment) и ret2win через Jinja2-шаблоны на основе JSON-отчета.
- 🛡️ **Анализ защит:** Автоматический checksec (PIE, Canary, NX, RELRO, Stripped).
- 🔍 **Поиск уязвимостей:** Сканирование PLT/GOT на опасные функции (gets, printf, strcpy, system).
-  **Auto Offset Finder:** Автоматический расчет смещения до EIP/RIP с помощью cyclic pattern и GDB.
- 📝 **Format String Analyzer:** Автопоиск смещения пользовательского ввода в стеке.
- 🛡️ **Canary Bypass Analyzer:** Точный GDB-анализ структуры стека функции для математически выверенного обхода Stack Canary.
- 🌐 **REST API & Python Client:** Возможность запуска анализа удаленно через API или удобный CLI-клиент.

## 📦 Установка и запуск (Docker)

Самый простой и надежный способ запустить инструмент на любой ОС, так как все зависимости уже включены в образ.

```bash
git clone https://github.com/madcap-syd/pwn-automation-tool.git
cd pwn-automation-tool

# Сборка образа
docker build -t pwn-auto .

# Полный анализ бинарника
docker run --rm -v $(pwd):/app pwn-auto analyze ./target_binary

# Автоматический поиск смещения BOF
docker run --rm -v $(pwd):/app pwn-auto find-offset ./target_binary

# Анализ стека для обхода Canary
docker run --rm -v $(pwd):/app pwn-auto bypass-canary ./target_binary
```

> 💡 Флаг -v $(pwd):/app подключает твою текущую папку внутрь контейнера, чтобы инструмент видел твои файлы.

##  Локальный запуск (без Docker)

Требует ОС Linux (рекомендуется Kali Linux), Python 3.8+, GDB, Radare2 и (опционально) Ghidra.

```bash
# 1. Установка системных зависимостей (для Kali/Debian)
sudo apt update
sudo apt install python3-venv gdb radare2 ghidra

# 2. Настройка окружения
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

# 3. Запуск инструмента
python3 main.py analyze ./target_binary
python3 main.py solve-keygen ./keygenme
python3 main.py help
```

## 🦑 Использование Ghidra Analyzer

Новый мощный модуль для глубокой декомпиляции без ручного запуска GUI:

```bash
# Быстрый анализ C/C++ бинарника (таймаут 120 сек)
python3 ghidra_analyzer.py ./vuln

# Анализ сложных бинарников (Rust/Go) с увеличенным таймаутом (600 сек)
python3 ghidra_analyzer.py ./rust_binary --rust

# Ручная настройка таймаута и сохранение подробного отчета в Markdown
python3 ghidra_analyzer.py ./target --timeout 300 --report analysis.md
```

## 🌐 Использование API и Клиента

Фреймворк включает в себя FastAPI сервер и Python-клиент для автоматизации в пайплайнах.

```bash
# Запуск API сервера
python3 api_server.py

# Удаленный анализ через клиент
python3 client.py analyze http://localhost:8000 ./target_binary
```

## 📂 Структура проекта

```text
pwn-automation-tool/
├── main.py                      # Точка входа CLI
├── ghidra_analyzer.py           # 🆕 Модуль автоматического анализа через Ghidra Headless
├── test_ghidra_analyzer.py      # 🆕 Тестовый скрипт для Ghidra модуля
── api_server.py                # FastAPI сервер
── client.py                    # Python клиент для API
── src/                         # Модули автоматизации (Radare2, SAST, генераторы эксплойтов)
├── modules/                     # Специализированные солверы (BOF, Canary, Format String, Keygen)
├── ghidra_scripts/              # 🆕 Java и Jython скрипты для Ghidra headless режима
├── WRITEUPS/                    # 🆕 База знаний и разборы решенных задач (Markdown)
├── output/                      # Директория для JSON-отчетов и артефактов
├── Dockerfile                   # Конфигурация Docker-образа
└── requirements.txt             # Зависимости Python
```

## 🤝 Вклад в проект

Pull Requests приветствуются! Для серьезных изменений, пожалуйста, сначала откройте Issue, чтобы обсудить, что вы хотите изменить.

## 📜 Лицензия

Этот проект распространяется под лицензией MIT. Используйте ответственно и только в образовательных целях или на легальных CTF-площадках.

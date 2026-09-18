# Используем легкий образ Python
FROM python:3.10-slim

# Устанавливаем системные зависимости для реверса и эксплойтов
# (gdb для поиска смещений, binutils для objdump, gcc для компиляции тестов)
RUN apt-get update && apt-get install -y \
    gdb \
    binutils \
    gcc \
    gcc-multilib \
    git \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код инструмента
COPY . .

# Делаем главный скрипт исполняемым
RUN chmod +x main.py

# Точка входа: по умолчанию запускаем наш инструмент
ENTRYPOINT ["python3", "main.py"]

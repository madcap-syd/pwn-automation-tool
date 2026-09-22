FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    gdb \
    binutils \
    gcc \
    gcc-multilib \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# ВАЖНО: Запускаем именно API-сервер (FastAPI), а не main.py
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]

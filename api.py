from fastapi import FastAPI, UploadFile, File, HTTPException
import subprocess
import os
import tempfile
import re

app = FastAPI(
    title="Pwn Automation API",
    description="API для автоматического анализа бинарных файлов на уязвимости",
    version="1.1.0" # Обновили версию
)

def run_tool(command: list, tmp_path: str) -> dict:
    """Вспомогательная функция для запуска main.py"""
    try:
        os.chmod(tmp_path, 0o755)
        
        result = subprocess.run(
            ["python3", "main.py"] + command + [tmp_path],
            capture_output=True,
            text=True,
            timeout=60 # Увеличили таймаут, так как GDB может думать
        )
        
        return {
            "status": "success" if result.returncode == 0 else "error",
            "raw_output": result.stdout,
            "errors": result.stderr if result.stderr else None
        }
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=500, detail="Анализ занял слишком много времени (таймаут GDB)")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze")
async def analyze_binary(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix="_binary") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    try:
        result = run_tool(["analyze"], tmp_path)
        return {
            "filename": file.filename,
            **result
        }
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)

@app.post("/find-offset")
async def find_offset_binary(file: UploadFile = File(...)):
    """Загружает бинарник, ищет смещение через GDB и возвращает результат + распарсенное число"""
    with tempfile.NamedTemporaryFile(delete=False, suffix="_binary") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    try:
        result = run_tool(["find-offset"], tmp_path)
        
        # Пытаемся найти число смещения в выводе с помощью регулярного выражения
        # Ищем фразу: "Найдено смещение до адреса возврата: 112 байт!"
        match = re.search(r"Найдено смещение до адреса возврата:\s*(\d+)\s*байт", result["raw_output"])
        parsed_offset = int(match.group(1)) if match else None
        
        return {
            "filename": file.filename,
            "parsed_offset": parsed_offset, # Новое поле!
            **result
        }
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)

@app.get("/")
async def root():
    return {"message": "Pwn Automation API v1.1 is running! Use POST /analyze or /find-offset"}

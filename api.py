from fastapi import FastAPI, UploadFile, File, HTTPException
import subprocess
import os
import tempfile

app = FastAPI(
    title="Pwn Automation API",
    description="API для автоматического анализа бинарных файлов на уязвимости",
    version="1.0.0"
)

@app.post("/analyze")
async def analyze_binary(file: UploadFile = File(...)):
    """Загружает бинарник и возвращает полный анализ в формате JSON"""
    
    # Создаем временный файл для загруженного бинарника
    with tempfile.NamedTemporaryFile(delete=False, suffix="_binary") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    try:
        # Делаем файл исполняемым
        os.chmod(tmp_path, 0o755)
        
        # Запускаем наш main.py через subprocess
        result = subprocess.run(
            ["python3", "main.py", "analyze", tmp_path],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Формируем ответ
        return {
            "filename": file.filename,
            "status": "success" if result.returncode == 0 else "error",
            "analysis_output": result.stdout,
            "errors": result.stderr if result.stderr else None
        }
        
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=500, detail="Анализ занял слишком много времени")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Удаляем временный файл
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)

@app.get("/")
async def root():
    return {"message": "Pwn Automation API is running! Use POST /analyze to upload a binary."}

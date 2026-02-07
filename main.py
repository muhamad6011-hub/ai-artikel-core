# ===========================
# 1️⃣ Masuk folder project
# ===========================
cd C:\AI-ARTIKEL

# ===========================
# 2️⃣ Buat / update main.py di folder app
# ===========================
$mainPy = @"
from fastapi import FastAPI, Request
from pathlib import Path
import json

app = FastAPI()

# Folder artikel-01 sampai artikel-05
ARTIKEL_FOLDERS = [Path(f""artikel-0{i}"") for i in range(1,6)]

def search_bigdata(question: str) -> str:
    question_lower = question.lower()
    for folder in ARTIKEL_FOLDERS:
        artikel_file = folder / ""artikel.txt""
        if artikel_file.exists():
            content = artikel_file.read_text(encoding=""utf-8"")
            if question_lower in content.lower():
                start_index = content.lower().find(question_lower)
                snippet = content[start_index:start_index+300]
                return snippet + ""...""
    return ""Maaf, saya belum menemukan jawaban yang sesuai di dataset.""

@app.post(""/ask"")
async def ask(request: Request):
    data = await request.json()
    question = data.get(""question"", """")
    answer = search_bigdata(question)
    return {""question"": question, ""answer"": answer}

if __name__ == ""__main__"":
    import uvicorn
    uvicorn.run(app, host=""0.0.0.0"", port=8000)
"@

# Tulis main.py
$mainPy | Out-File -Encoding UTF8 app\main.py

# ===========================
# 3️⃣ Install dependencies
# ===========================
pip install fastapi uvicorn

# ===========================
# 4️⃣ Push ke GitHub otomatis
# ===========================
git add .
git commit -m "Update main.py /ask route"
git push origin main

# ===========================
# 5️⃣ Jalankan Replit via API (via shell)
# ===========================
# Pastikan Replit sudah terhubung GitHub (Auto deploy)
# Jalankan server di Replit:
# Di Replit, run command akan otomatis ambil main.py terbaru dari GitHub

Write-Host "Server FastAPI siap. Blogspot B bisa memanggil /ask di Replit API."

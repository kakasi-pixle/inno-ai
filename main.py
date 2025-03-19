import os
from fastapi import FastAPI
from model import chat  # استدعاء الذكاء الاصطناعي

# تثبيت المكتبات تلقائيًا عند تشغيل الكود
os.system("pip install -r requirements.txt")

app = FastAPI()

@app.get("/inno-ai/")
def chat_api(prompt: str):
    response = chat(prompt)
    return {"response": response}

# تشغيل السيرفر
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

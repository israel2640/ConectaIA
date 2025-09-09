# app/main.py

from fastapi import FastAPI
# Removido: from app.api import whatsapp
from app.api import telegram # Mantemos apenas a importação do Telegram

app = FastAPI(
    title="ConectaIA Bot",
    description="API para automatizar respostas no Telegram com IA.",
    version="1.0.0"
)

# Removido: app.include_router(whatsapp.router)
app.include_router(telegram.router) # Mantemos apenas o router do Telegram

@app.get("/", tags=["Root"])
async def root():
    return {"message": "API do ConectaIA está no ar!"}
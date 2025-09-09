# app/api/telegram.py

from fastapi import APIRouter, Request
from app.services.telegram_service import send_message
from app.services.openai_service import gerar_resposta_ia
# Importamos as novas funções do supabase
from app.services.supabase_service import salvar_mensagem, buscar_historico
import json

router = APIRouter(
    prefix="/telegram",
    tags=["Telegram"],
)

@router.post("/webhook")
async def handle_webhook(request: Request):
    try:
        data = await request.json()

        print("\n--- Webhook Recebido do Telegram ---")
        print(json.dumps(data, indent=2))
        print("------------------------------------\n")

        mensagem = data.get("message", {})
        chat_id = mensagem.get("chat", {}).get("id")
        texto_usuario = mensagem.get("text")

        if texto_usuario and chat_id:
            # 1. SALVAR A MENSAGEM DO USUÁRIO
            await salvar_mensagem(chat_id=chat_id, role="user", content=texto_usuario)

            # 2. BUSCAR O HISTÓRICO RECENTE
            historico = await buscar_historico(chat_id=chat_id)

            # 3. GERAR RESPOSTA COM CONTEXTO
            resposta_ia = gerar_resposta_ia(
                mensagem_usuario=texto_usuario,
                historico_conversa=historico # Passamos o histórico para a IA
            )
            print(f"Resposta da IA com contexto: {resposta_ia}")

            # 4. ENVIAR RESPOSTA PARA O USUÁRIO
            await send_message(chat_id=chat_id, text=resposta_ia)

            # 5. SALVAR A RESPOSTA DO BOT
            await salvar_mensagem(chat_id=chat_id, role="assistant", content=resposta_ia)

    except Exception as e:
        print(f"Ocorreu um erro no processamento do webhook: {e}")

    return {"status": "ok"}
# app/services/telegram_service.py

import httpx
from app.core.config import settings

# Montamos a URL base da API do Telegram.
TELEGRAM_API_URL = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}"

async def send_message(chat_id: int, text: str):
    """
    Envia uma mensagem de texto para um chat específico do Telegram.
    """
    # O payload (corpo) da nossa requisição.
    payload = {
        "chat_id": chat_id,
        "text": text
    }

    try:
        # Usamos um cliente async para fazer a requisição HTTP.
        async with httpx.AsyncClient() as client:
            print(f"Enviando mensagem para o chat_id: {chat_id}")
            response = await client.post(f"{TELEGRAM_API_URL}/sendMessage", json=payload)

            # Verifica se a requisição foi bem-sucedida
            if response.status_code == 200:
                print("Mensagem enviada com sucesso!")
            else:
                print(f"Erro ao enviar mensagem: {response.status_code}")
                print(response.json())

            return response

    except Exception as e:
        print(f"Ocorreu um erro na requisição: {e}")
        return None
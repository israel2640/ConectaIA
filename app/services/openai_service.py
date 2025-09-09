# app/services/openai_service.py

from openai import OpenAI
from app.core.config import settings

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=settings.OPENAI_API_KEY)

def gerar_resposta_ia(mensagem_usuario: str, historico_conversa: list = None):
    """
    Sends the user's message and history to OpenAI and returns the GPT response.
    """
    if historico_conversa is None:
        historico_conversa = []

    # Define the persona of your assistant (the "system prompt")
    prompt_sistema = {
        "role": "system",
        "content": (
            "Você é um assistente virtual chamado ConectaIA. "
            "Sua principal função é ajudar os clientes de forma rápida e amigável. "
            "Seja sempre educado e direto nas suas respostas. "
            "Não invente informações que você não sabe."
        )
    }

    # Assemble the message structure for the API
    mensagens = [prompt_sistema] + historico_conversa + [{
        "role": "user",
        "content": mensagem_usuario
    }]

    try:
        # Make the call to the OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=mensagens,
            temperature=0.7,
            max_tokens=150
        )

        # Extract the text response from the API response object
        resposta_assistente = response.choices[0].message.content
        return resposta_assistente.strip()

    except Exception as e:
        # In case of an OpenAI API error, return a default message
        print(f"Erro ao chamar a API da OpenAI: {e}")
        return "Desculpe, estou com um problema no momento. Tente novamente mais tarde."
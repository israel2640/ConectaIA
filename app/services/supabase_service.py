# app/services/supabase_service.py

from supabase import create_client, Client
from app.core.config import settings

# Inicializa o cliente do Supabase com as nossas chaves do .env
supabase_url: str = settings.SUPABASE_URL
supabase_key: str = settings.SUPABASE_KEY
supabase: Client = create_client(supabase_url, supabase_key)

async def salvar_mensagem(chat_id: int, role: str, content: str):
    """
    Salva uma mensagem (do usuário ou do assistente) no banco de dados.
    """
    try:
        print(f"Salvando mensagem para chat_id {chat_id}: Role='{role}'")
        # Insere um novo registro na tabela 'historico_conversas'
        supabase.table("historico_conversas").insert({
            "chat_id": chat_id,
            "role": role,
            "content": content
        }).execute()
        print("Mensagem salva com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar mensagem no Supabase: {e}")

async def buscar_historico(chat_id: int, limite: int = 10):
    """
    Busca as últimas mensagens de uma conversa específica no banco de dados.
    """
    try:
        print(f"Buscando histórico para chat_id {chat_id}...")
        # Busca os registros da tabela, ordenando pelos mais recentes
        response = supabase.table("historico_conversas") \
            .select("role", "content") \
            .eq("chat_id", chat_id) \
            .order("created_at", desc=True) \
            .limit(limite) \
            .execute()

        # Os dados vêm na ordem do mais novo para o mais antigo, então invertemos
        historico_formatado = list(reversed(response.data))
        print("Histórico encontrado:", historico_formatado)
        return historico_formatado
    except Exception as e:
        print(f"Erro ao buscar histórico no Supabase: {e}")
        return []
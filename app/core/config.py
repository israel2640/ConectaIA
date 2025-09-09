# app/core/config.py

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Carrega as variáveis do arquivo .env
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # WHATSAPP_VERIFY_TOKEN: str <-- Linha removida

    OPENAI_API_KEY: str
    SUPABASE_URL: str
    SUPABASE_KEY: str
    TELEGRAM_BOT_TOKEN: str

# Cria uma instância das configurações que será usada no resto do app
settings = Settings()
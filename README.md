# 🤖 ConectaIA - Chatbot Inteligente para Telegram

![Status do Projeto](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Framework](https://img.shields.io/badge/framework-FastAPI-green)

Um chatbot com IA para Telegram, projetado para automatizar atendimentos e otimizar a comunicação com clientes, utilizando o poder da OpenAI para respostas inteligentes e contextuais.

## ✨ Funcionalidades Principais

* **Inteligência Artificial Conversacional:** Utiliza a API da OpenAI (GPT-3.5) para entender e responder às perguntas dos usuários de forma natural e humana.
* **Memória Persistente:** Integração com o Supabase (PostgreSQL) para salvar o histórico das conversas, permitindo que o bot tenha conversas com contexto e se lembre de interações anteriores.
* **Integração com Telegram:** Comunicação em tempo real através da API de Bots do Telegram.
* **API Robusta e Assíncrona:** Construído com FastAPI, garantindo alta performance para receber e processar um grande volume de mensagens.

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python 3.10+
* **Framework API:** FastAPI
* **Inteligência Artificial:** OpenAI API
* **Banco de Dados:** Supabase (PostgreSQL)
* **Comunicação:** Telegram Bot API
* **Servidor de Desenvolvimento:** Uvicorn
* **Túnel Local:** Ngrok
* **Bibliotecas Principais:** `httpx`, `pydantic-settings`, `supabase-py`

## 🚀 Guia de Instalação e Execução

Siga os passos abaixo para configurar e rodar o projeto em seu ambiente local.

### 1. Pré-requisitos

* Python 3.10 ou superior
* Conta na [OpenAI](https://openai.com/) para obter uma chave de API.
* Conta no [Supabase](https://supabase.com/) para criar um banco de dados.
* Conta no [Telegram](https://telegram.org/) e um bot criado através do [@BotFather](https://t.me/BotFather).
* [Ngrok](https://ngrok.com/download) para expor sua API localmente.

### 2. Clonar o Repositório

```bash
git clone [URL_DO_SEU_REPOSITORIO_NO_GITHUB]
cd ConectaIA
```

### 3. Configurar o Ambiente Virtual

```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente (Windows)
.\venv\Scripts\Activate
```

### 4. Instalar as Dependências

```bash
pip install -r requirements.txt
```

### 5. Configurar as Variáveis de Ambiente

1.  Renomeie o arquivo `.env.example` para `.env`.
2.  Abra o arquivo `.env` e preencha com suas chaves e URLs:

```ini
OPENAI_API_KEY="sk-..."
SUPABASE_URL="[https://seu-projeto.supabase.co](https://seu-projeto.supabase.co)"
SUPABASE_KEY="sua-chave-anon-publica-do-supabase"
TELEGRAM_BOT_TOKEN="seu-token-do-botfather"
```

### 6. Preparar o Banco de Dados

Execute o script SQL necessário no **SQL Editor** do seu projeto Supabase para criar a tabela de histórico. O script está [neste link](URL_PARA_O_SCRIPT_SE_ESTIVER_EM_OUTRO_ARQUIVO) ou pode ser copiado do código-fonte.

### 7. Rodar o Projeto

Você precisará de dois terminais abertos.

**No Terminal 1 (Inicie a API):**

```bash
uvicorn app.main:app --reload
```

**No Terminal 2 (Inicie o Ngrok):**

```bash
# Se o ngrok.exe estiver na pasta
.\ngrok http 8000

# Se estiver instalado globalmente
ngrok http 8000
```

### 8. Configurar o Webhook do Telegram

1.  Copie a URL `https` gerada pelo ngrok.
2.  Acesse a seguinte URL no seu navegador, substituindo as variáveis:
    `https://api.telegram.org/bot[SEU_TOKEN]/setWebhook?url=[SUA_URL_NGROK]/telegram/webhook`

## 📝 Próximos Passos (To-Do)

-   [ ] Implementar um painel de controle administrativo para visualizar conversas.
-   [ ] Adicionar indicador de "digitando..." para melhor experiência do usuário.
-   [ ] Criar um sistema de logs mais robusto.
-   [ ] Expandir para outros canais (ex: WhatsApp).

## 👨‍💻 Autor

* **Israel** 
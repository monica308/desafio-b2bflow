import os
import requests
from dotenv import load_dotenv
from supabase import create_client

# 1. Carrega as variáveis de ambiente
load_dotenv()

URL_DO_SUPABASE = os.getenv("SUPABASE_URL")
CHAVE_DO_SUPABASE = os.getenv("SUPABASE_KEY")
ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")

# 2. Conecta ao Supabase
supabase = create_client(URL_DO_SUPABASE, CHAVE_DO_SUPABASE)

print("Buscando contatos no banco de dados...")
resposta = supabase.table("contatos").select("*").execute()
lista_contatos = resposta.data

# 3. Loop para enviar a mensagem para cada contato encontrado
for contato in lista_contatos:
    nome = contato.get("nome")
    telefone = contato.get("telefone")
    
    # Criando uma mensagem personalizada
    mensagem = f"Olá, {nome} tudo bem com você?"
    
    print(f"Enviando mensagem para {nome} ({telefone})...")
    
    # URL de envio da Z-API
    url_zapi = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text"
    
    # Dados que a Z-API precisa receber
    payload = {
        "phone": telefone,
        "message": mensagem
    }
    
    # Cabeçalho da requisição
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        # Faz o disparo da mensagem
        retorno = requests.post(url_zapi, json=payload, headers=headers)
        
        if retorno.status_code == 200:
            print(f"Sucesso! Mensagem enviada para {nome}.")
        else:
            print(f"Erro ao enviar para {nome}: Status {retorno.status_code} - {retorno.text}")
            
    except Exception as e:
        print(f"Falha na conexão ao tentar enviar para {nome}: {e}")

print("\nProcesso de automação finalizado!")
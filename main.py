import os
from dotenv import load_dotenv
from supabase import create_client

# 1. Carrega as chaves no arquivo .env
load_dotenv()

URL_DO_SUPABASE = os.getenv("SUPABASE_URL")
CHAVE_DO_SUPABASE = os.getenv("SUPABASE_KEY")

# 2. Conecta com o site do Supabase as chaves
supabase = create_client(URL_DO_SUPABASE, CHAVE_DO_SUPABASE)

print("Conectando ao banco de dados...")

# 3. Faz a busca na tabela de contatos
resposta = supabase.table("contatos").select("*").execute()

# 4. Mostra na tela os dados 
print("\n--- CONTATOS ENCONTRADOS NO BANCO ---")
print(resposta.data)
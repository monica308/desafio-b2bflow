# Desafio Automação B2BFlow 🚀

Este projeto consiste em uma automação desenvolvida em Python para ler contatos armazenados em um banco de dados na nuvem (Supabase) e disparar mensagens personalizadas via WhatsApp utilizando a API da Z-API.

## 🛠️ Tecnologias Utilizadas

- **Python 3.14+**
- **Supabase** (Banco de dados PostgreSQL na nuvem)
- **Z-API** (API de integração com o WhatsApp)
- **Bibliotecas Python:** `supabase`, `python-dotenv`, `requests`

## 📋 Pré-requisitos e Setup do Banco de Dados

### 1. Estrutura da Tabela no Supabase
No seu painel do Supabase, crie uma tabela chamada `contatos` com a seguinte estrutura de colunas:

| Coluna | Tipo | Descrição |
| :--- | :--- | :--- |
| `id` | int8 (Primary Key) | Identificador único (Gerado automaticamente) |
| `created_at` | timestamptz | Data de criação (Gerado automaticamente) |
| `nome_contato` | text | Nome completo do contato |
| `telefone` | text | Número com DDI + DDD + Número (ex: `5531994998935`) |


## ⚙️ Configuração do Ambiente Local

### 1. Clonar e criar o Ambiente Virtual (venv)

Primeiro, abra o terminal no seu computador e clone o projeto com o comando abaixo (substitua pelo link real do seu repositório):

git clone https://github.com/monica308/desafio-b2bflow.git

No terminal do seu VS Code, execute os comandos abaixo para isolar as dependências do projeto:

Bash
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual (Windows)
.\\venv\\Scripts\\activate

### 2.Instalar as Dependências

Bash
python -m pip install supabase python-dotenv requests

### 3. Variáveis de Ambiente (.env)
O projeto utiliza variáveis de ambiente para garantir a segurança das credenciais. Crie um arquivo chamado .env na raiz do projeto (este arquivo está listado no .gitignore por motivos de segurança e não é enviado ao repositório).

Configure as seguintes chaves:

SUPABASE_URL=[https://seu-projeto.supabase.co](https://seu-projeto.supabase.co)
SUPABASE_KEY=sua-chave-anon-public-do-supabase
ZAPI_INSTANCE_ID=seu-id-da-instancia-zapi
ZAPI_TOKEN=seu-token-da-instancia-zapi

### O que o script faz:
Conecta com segurança ao banco de dados Supabase utilizando as variáveis de ambiente.

Faz o download de todos os registros da tabela contatos.

Percorre cada contato e monta a mensagem personalizada: "Olá, <nome_contato> tudo bem com você?".

Dispara a mensagem via requisição HTTP POST para a API da Z-API.


📸 Evidências de Funcionamento:

<img width="553" height="606" alt="WhatsApp Image 2026-06-23 at 15 04 29" src="https://github.com/user-attachments/assets/382c13ab-1eef-4e63-97a9-0ee8998a0db1" />

Desenvolvido por Mônica Araújo

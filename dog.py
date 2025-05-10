import requests
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do .env
load_dotenv()

# Obter a API Key do ambiente
api_key = os.getenv('DOG_API_KEY')

# URL da rota de busca de imagem
url = 'https://api.thedogapi.com/v1/images/search'

# Cabeçalhos para autenticação
headers = {
    'x-api-key': api_key
}

# Realizar a requisição GET
response = requests.get(url, headers=headers)

# Verificar se a resposta foi bem sucedida
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Erro ao buscar imagem: {response.status_code} - {response.text}")
import requests
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do .env
load_dotenv()

# Obter a API Key do ambiente
api_key = os.getenv('NEWS_API_KEY')

# Endpoint da NewsAPI (rota EVERYTHING)
url = "https://newsapi.org/v2/everything"

# Cabeçalhos para autenticação
headers = {
    'x-api-key': api_key
}

params = { 
    'q' : 'Python',
    'language' : 'pt',
    'page' : '2'
}

# Realizar a requisição GET
resposta = requests.get(url, headers=headers, params=params)

print(resposta.status_code)

resposta_json = resposta.json()
print(resposta.json())

print(resposta_json['articles'][7]['source']['name'])

for artigo in resposta_json['articles'][:10]:
    print('\n')
    print(artigo['title'])
    print(artigo['description'])
    print(artigo['url'])



if not api_key:
    raise ValueError('API Key não foi localizada nas variáveis de ambiente.')


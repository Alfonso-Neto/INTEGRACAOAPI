import requests
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do .env
load_dotenv()

# Obter a API Key do ambiente
api_key = os.getenv('WEATHER_API_KEY')

if not api_key:
    raise ValueError('API Key não foi localizada nas variáveis de ambiente.')

url = 'https://api.openweathermap.org/data/2.5/weather'

cidade1 = input('Digite a primeira cidade BRASILEIRA para ver o clima: ')
cidade2 = input('Digite a segunda cidade BRASILEIRA para ver o clima: ')

cidades = [f'{cidade1},BR', f'{cidade2},BR']



for cidade in cidades:
    params = {
    'q': cidade,   
    'appid': api_key,      
    'units': 'metric',      
    'lang': 'pt_br'        
    }
 
    # Fazer a requisição GET
    resposta = requests.get(url, params=params)

    print(resposta.status_code)

    resposta_json = resposta.json()
    print(resposta.json())
    clima = resposta_json['weather'][0]['description']
    temperatura = resposta_json['main']['temp']

    print(clima)
    print(temperatura)



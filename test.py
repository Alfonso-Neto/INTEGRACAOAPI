import requests
import os
from dotenv import load_dotenv

def consultar_clima():
    # Carregar variáveis de ambiente do .env
    load_dotenv()

    # Obter a API Key do ambiente
    api_key = os.getenv('WEATHER_API_KEY')

    if not api_key:
        raise ValueError('API Key não foi localizada nas variáveis de ambiente.')

    url = 'https://api.openweathermap.org/data/2.5/weather'

    # Entrada de cidades
    cidades = [
        input('Digite a primeira cidade para ver o clima: '),
        input('Digite a segunda cidade para ver o clima: '),
        input('Digite a terceira cidade para ver o clima: ')
    ]

    temperaturas = {}

    for cidade in cidades:
        params = {
            'q': cidade,
            'appid': api_key,
            'units': 'metric',
            'lang': 'pt_br'
        }

        resposta = requests.get(url, params=params)

        if resposta.status_code == 200:
            dados = resposta.json()
            clima = dados['weather'][0]['description']
            temperatura = dados['main']['temp']
            temperaturas[cidade] = temperatura

            print(f'\nCidade: {cidade}')
            print(f'Clima: {clima.capitalize()}')
            print(f'Temperatura: {temperatura:.1f}°C')
        else:
            print(f'\n❌ Não foi possível obter os dados de "{cidade}". Verifique o nome e tente novamente.')

    if temperaturas:
        cidade_mais_quente = max(temperaturas, key=temperaturas.get)
        print(f'\n🔥 A cidade mais quente é {cidade_mais_quente} com {temperaturas[cidade_mais_quente]:.1f}°C.')

consultar_clima()

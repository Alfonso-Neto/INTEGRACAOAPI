'''import requests

resposta_lista = requests.get('https://jsonplaceholder.typicode.com/posts')
resposta_unique = requests.get('https://jsonplaceholder.typicode.com/posts/1')

posts = resposta_lista.json()
post_1 = resposta_unique.json()
print('Tipo de lista (vários posts): ', type(posts))
print('Tipo único (um só post): ', type(post_1))


for post in posts[ :10]:
    print('Título: ', post['title'])
    print('Conteúdo: ', post['body'])'''

import requests

def criar_post(codigo):
    url = f'https://jsonplaceholder.typicode.com/posts/{codigo}'
    novo_post = {
    "title": 'My title',
    "body": 'My content',
    "userId": "33",
    }

    resposta = requests.put(url, json=novo_post)
    print(resposta.status_code)
    resultado_api = resposta.json()
    print(resultado_api)

def visualizar_post(codigo):
    url = f'https://jsonplaceholder.typicode.com/posts/{codigo}'
    resposta = requests.get(url)
    print(resposta.status_code)
    resultado_api = resposta.json()
    print(resultado_api)

def atualizar_post(codigo):
    url = f'https://jsonplaceholder.typicode.com/posts/{codigo}'
    novo_post = {
    "title": 'My title',
    }

    resposta = requests.patch(url, json=novo_post)
    print(resposta.status_code)
    resultado_api = resposta.json()
    print(resultado_api)

visualizar_post(1)
criar_post(1)
atualizar_post(1)


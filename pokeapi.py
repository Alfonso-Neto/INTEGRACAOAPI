import requests

def buscar_pokemons(qntd):
    resposta_lista = requests.get(f"https://pokeapi.co/api/v2/pokemon?limit={qntd}")
    resposta = resposta_lista.json()
    
    pokemons = resposta['results']
    for pokemon in pokemons:
        print(pokemon["name"])

quantidade = input('Digite a quantidade de pokemons para buscar: ')
buscar_pokemons(quantidade)
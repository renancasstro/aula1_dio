import pandas as pd
import numpy as np
import requests

def pokemon_search(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    pokemon_data = response.json()
    return pokemon_data


pokemon = input('Insira seu Pokemon: ')
#Como a busca é feita em lowercase, é necessário utilizar o comando lower()
pokemon = pokemon.lower()
pokemon_data = pokemon_search(pokemon)
nome = pokemon_data['species']['name'].capitalize()
print(nome)
# print(pokemon_data['sprites']['front_default'])
# print(pokemon_data['moves'][0]['move']['name'])
print('Moves: \n')
n = 0
y = []
while True:
    try:
        x = [pokemon_data['moves'][n]['move']['name'].capitalize()]
        y.append(x)
        n += 1
    except IndexError:
        break
print(y)

    




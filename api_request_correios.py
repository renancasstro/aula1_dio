import pandas as pd
import numpy as np
import requests

def retorna_dados_cep(cep):
    response = requests.get('http://viacep.com.br/ws/{}/json'.format(cep))
    dados_cep = response.json()
    print(dados_cep)
    return dados_cep
labels = [1]

cep = input('Insira um CEP: ')
data = retorna_dados_cep(cep)
df = pd.DataFrame(data=data, index=labels)
print(df)
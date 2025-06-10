import requests
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

headers = {
    'Authorization' : f"Bearer {os.getenv('token_autenticacao')}",
    'User-Agent' : 'HnunesDev'
}
url = 'https://api.github.com/users/HNunesDev/repos'

resposta = requests.get(url, headers=headers)
print(resposta.headers['Content-Type']) #Se for realmente uma api retorna application/json;
if resposta.status_code == 200:
    repos = resposta.json()
    for repo in repos:
        print(f'Repostirio_name: {repo['name']}')
else:
    print(f'Erro na requisiçao {resposta.status_code}')

# print(resposta.json())
df = resposta.json()

for repo in repos:
    if 'Alura' in repo['name']:
        print(f'Descricao do repositorio Alura: {repo['description']}')
        print(f"{repo['owner']['login']} é o proprietario do repostirório Alura")
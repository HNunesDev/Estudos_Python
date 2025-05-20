import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dados_idade_aposentadoria = pd.read_csv('Conceitos/testando_hipoteses/dados_idade_aposentadoria.csv')
dados_vida_lamapada = pd.read_csv('Conceitos/testando_hipoteses/dados_vida_lampada.csv')
dados_alturas = pd.read_csv('Conceitos/testando_hipoteses/dados_alturas.csv')


n = 100 #-> tamanho da amostra
qtd = 10000 #-> quantidade de amostras

#Criando uma funcao para realizar reamostragem
def reamostragem_meida(dados, coluna, n, qtd):
    meidas = [dados[coluna].sample(n, replace=True).mean() for _ in range(qtd)]
    return meidas


meida_idade = reamostragem_meida(dados_idade_aposentadoria, 'idade', n, qtd)
media_duracao = reamostragem_meida(dados_vida_lamapada, 'duracao', n, qtd)
meida_altura = reamostragem_meida(dados_alturas, 'alturas', n, qtd)
print(dados_vida_lamapada['duracao'].mean())

#transformando a media duracao em df
duracao_amostra = pd.DataFrame({'media_duracao : ': media_duracao})

"""
Anotacoes sobre o trecho estudado no curso

'Foi observado que em uma amostra a duracao da vida das lampadas estva por volta de 1200h, e sabemos que nossa media é por volta de 1731h, devemos realizar um teste
para comprovar se a a media mudou ou se a amostra foi apenas um acaso e devemos acionar a area de qualidade'

O parametro que se utiliza nesse caso é o Erro padrao.
Para descobrir o erro padrao, EP = duracao_amostra['media_duracao'].std() -> isso retorna o desvio padrao,e assim podemos calcular a quantidade de dados dentro do erro padrao
Utilizou-se o erro padrao para calcular o intervalo de confianca, e nesse caso foi +- 3*EP e viu que aproximadamente 98% dos dados estavam dentro desse intervalo.
Outra forma de calcular o erro padrao é utilizando from scipy import stats

Após isso, foi plotado um grafico sinalizando a media e o intervalo de confianca

media_das_meias = duracao_amostra['media_duracao'].mean() -> isso retorna a media das medias que é utilizado abaixo para calcular o intervalo de confianca

E para checar a quantidade de dados que estavam dentro do intervalo de confianca, foi utilizado o comando:
qnt_obs = duracao_amostra[(duracao_amostra > media_das_medias - 3*EP) & (duracao_amostra < media_das_meias + 3*EP)].count()]
qnt_obs.count()/duracao_amostra.count() -> isso retorna a quantidade de dados que estavam dentro do intervalo de confianca, e assim podemos ver se a amostra foi um acaso ou se realmente houve uma mudanca na media
"""

"""
Intervalo de confianca
Dando sequencia na proxima aula, foi dito sobre intervalo de confiança, e como ele é composto por 3 partes:
1 - A duraçao media
2 - O nivel de confianca
3 - O variabilidade dos meus dados

Foi utilizado a biblioteca stats do scipy
É levado em consideracao o primeiro df carregado (aqui no exemplo da atividade)
E o nivel de confianca foi locado em 95 -> confianca = 0.95

Pegando os dados para calcular o intervalo de confianca:
media = dados_vida_lamapada['duracao'].mean()
desvio_padrao_amostra = dados_vida_lamapada['duracao'].std()
tamanho_amostra = len(dados_vida_lamapada)

Calculando o intervalo de confianca:
intervalo_confianca = stats.norm.interval(confianca, loc=media, scale=desvio_padrao_amostra/np.sqrt(tamanho_amostra)) -> parametros necessarios
intervalo_confianca -> retorna dois valores, o inferior e o superior do intervalo de confianca e caso a amostra esteja dentro desse intervalo, podemos dizer que a amostra é confiavel
"""
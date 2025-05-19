import pandas as pd
from scipy.stats import ttest_1samp
import numpy as np

""""
Techsafe é uma empresa de tecnologia que lançou recentemente um novo software de compressão de dados, 
alegando que ele é capaz de reduzir significativamente o tamanho dos arquivos em comparação com a versão anterior. 
A equipe de desenvolvimento está interessada em verificar se, de fato, o novo software alcança uma média de compressão superior a 20%, conforme anunciado.

Para essa tarefa, a Techsafe disponibilizou poucos dados amostrais em relação à sua última consultoria. 
A equipe recebeu uma amostra de 25 arquivos compactados usando o novo software e mediu a porcentagem de compressão para cada arquivo, armazenando cada valor em uma tabela com escala de 0 a 100.

"""
#H0: μ = 20
#H1: μ > 20

df_techsafe = pd.DataFrame({'porcentagem_compressao': [21.99342831, 20.7234714 , 22.29537708, 24.04605971, 20.53169325, 20.53172609, 24.15842563, 22.53486946, 20.06105123, 22.08512009, 20.07316461, 20.06854049, 21.48392454, 17.17343951, 17.55016433, 19.87542494, 18.97433776, 21.62849467, 19.18395185, 18.1753926, 23.93129754, 20.5484474 , 21.13505641, 18.15050363, 19.91123455]})

media_tech = np.mean(df_techsafe)
# print(media_tech) #-> 20.6729838832

nivel_confianca = 0.95
nivel_significancia = 0.05

status, p_valor = ttest_1samp(df_techsafe['porcentagem_compressao'], 20, alternative = 'greater')
print(status)
print(p_valor)

if p_valor < nivel_significancia:
    decisao = 'Rejeitar a hipótese nula'
else:
    decisao = 'Não rejeitar a hipótese nula'

print(f'Decisão: {decisao}')

#Perguntas a serem respondidas:
# Formule uma hipótese para o caso da Techsafe. - #H0: μ = 20 / #H1: μ > 20
# Calcule a média amostral dos dados. - 20.6729838832
# Estabeleça um nível de confiança para o problema e calcule o nível de significância. - 0.05
# Utilize o Teste t para calcular o valor da estatística t e o p-valor para o problema da Techsasfe, mostre os dados. - status 1.7588775656761988 / p_valor - 0.04567200091129674
# Pelos resultados anteriores, a hipótese nula formulada é rejeitada ou não rejeitada? Explique o que justifica sua decisão.
"""
Com base na anailise e nos testes realizados, por conta do p_valor(0.04) ser menor que o nivel de significancia(0.05) devemos rejeitar a hipotese nula 
"""

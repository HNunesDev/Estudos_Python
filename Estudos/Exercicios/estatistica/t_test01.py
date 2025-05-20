import pandas as pd
import numpy as np

# Problema proposto: 
# A Zoop está implementando um novo programa de treinamento para a equipe de vendas e deseja avaliar se ele resultou em um aumento nas vendas médias obtidas pelos vendedores e vendedoras. 
# O experimento envolveu medir os valores de vendas de cada pessoa vendedora antes e depois do treinamento.

df_equipe_vendas = pd.DataFrame({'Vendedor': [ 'Luíza', 'Bia', 'Rodrigo', 'Allan', 'Evaldo'],
                                 'Vendas Antes (R$)': [252.72, 203.91, 307.32, 185.78, 220.5],
                                 'Vendas Depois (R$)': [285.1, 223.15, 324.41, 202.23, 240.63]})

vendas_antes = df_equipe_vendas['Vendas Antes (R$)']
vendas_depois = df_equipe_vendas['Vendas Depois (R$)']
# print(vendas_antes)
# print(vendas_depois)
print(df_equipe_vendas)

#Perguntas a serem respondidas
#1- Defina a natureza das amostras. Temos um caso de amostra independente ou pareada?
#2- Formule uma hipótese para o primeiro caso da Zoop Megastore.
#3- Aplique um teste paramétrico para tomar a decisão da hipótese.
#4- Pelos resultados anteriores, a hipótese nula formulada é rejeitada ou não rejeitada? Explique o que justifica sua decisão.

#1R: Amostra pareada
#2R: H0: μ = 0 / H1: μ > 0
#3R: Feito
#4R: A H0 é rejeitada, pois o valor de p foi bem baixo, o que signifca que teve impacto significativo o treinamento


from scipy.stats import ttest_rel
stats, p_valor = ttest_rel(vendas_depois, vendas_antes, alternative = 'greater')
print(p_valor)



import pandas as pd

# Problema proposto:
# Além das vendas, a Zoop também gostaria de realizar um estudo sobre a satisfação do cliente em duas filiais diferentes que abriram recentemente. 
# O objetivo é determinar se há uma diferença significativa na pontuação média de satisfação do cliente entre as filiais.

df_filiais = pd.DataFrame({'Filial Centro-Norte': [3.2, 2.9, 2.0, 3.3, 3.1],
                           'Filial Sul': [3.8, 4.0, 4.7, 4.9, 4.8]})

Centro_norte = df_filiais['Filial Centro-Norte']
Sul = df_filiais['Filial Sul']

# Perguntas a serem respondidas:
#1 Defina a natureza das amostras. Temos um caso de amostra independente ou pareada?
#2 Formule uma hipótese para o segundo caso da Zoop Megastore.
#3 Aplique um teste paramétrico para tomar a decisão da hipótese.
#4 Pelos resultados anteriores, a hipótese nula formulada é rejeitada ou não rejeitada? Explique o que justifica sua decisão.

#1R: Independentes pois, são clientes diferentes
#2R: H0: μ = 0 / H1: μ != 0
#3R: Realizado
#4R: A H0 é rejeitada, pois o valor de p é bem baixo (0.001) o que colabora para rejeitarmos a H0 de que nao houve diferença significativa na pontuaçao media

from scipy.stats import ttest_ind

stats, p_valor = ttest_ind(Sul, Centro_norte)

print(stats)
print(p_valor)
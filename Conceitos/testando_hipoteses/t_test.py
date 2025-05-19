import numpy as np
from scipy.stats import ttest_1samp

"""
O Teste t é utilizado a partir de condicoes especificas 
1 - Tamanho da amostra é pequeno: Geralmente, o teste t é usado quando o tamanho da amostra (n) é menor que 30
2 - Desvio padrão populacional é desconhecido
3 - A amostra é aleatória e as observações são independentes
4 - A distribuição da população é aproximadamente normal ou o tamanho da amostra é suficientemente grande
"""

"""
Formulando outra hipotese:
1 - O tempo médio de respota do suporte tecnico é menor que 30 min

H0: μ = 30
H1: μ < 30
"""
tempo_resposta = [28, 32, 29, 31, 30, 33, 28, 30, 31, 29,
                  30, 32, 29, 31, 30, 33, 28, 30, 31, 29,
                  30, 32, 24, 29, 30]

media_resposta = np.mean(tempo_resposta)
print(media_resposta)

#Para esse caso iremos utilizar o t test, e ele é escolhido pois nao sabemos o numero da populacao e a amostra é menor que 30(25 neste caso)

#Para utilizar o t test é preciso de alguns parametros
# Amostra analisada = tempo_resposta
# Hipotese nula = 30
# Hipotese alternativa = 'less'

stats, p_valor = ttest_1samp(tempo_resposta, 30, alternative = 'less') # -> Retorna a estatistica do teste e o p valor
print(p_valor) #Probabilidade de observamos esta amostra em comparaçao ao todo
print(stats)

"""
Levando em conta o nivel de significancia de 5%, o p valor sendo maior. entao nao ha evidencias para rejeitar a H0 
"""


import numpy as np
from scipy.stats import ttest_1samp

"""
uma amostra
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

#Duas amostras -------------------------------

"""
É possivel tambem utiizar o test t para amostras INDEPENDENTES, no exemplo citado no curso. Eram duas amostras independentes de comprar do site, um para clientes que visualizaram
as propagandas e outro grupo que nao visualizou, e o H0 é que media sem propaganda = media com e H1 sem < com

Para utilizar de amostras independentes utiliza-se a lista dos valores de cada amostra (ex, sem_vendas, com_vendas) e utilizou ttest_ind
from scipy.stats import ttest_ind
ttest_ind(com_vendas, sem_vendas, alternative='greater') -> passase as duas amostras como parametros

Mesma coisa, retorna dois valores, um do estudo em si e o outro o p_valor que comparamos com base nele conseguimos contestar ou nao a H0

"""
"""
Amostras Pareadas -> sempre existe um par para comparar, no exemplo do curso os funcionarios avaliaram um processo da empresa x e após realizar o treinamento reaviliaram o processo
ou seja, as duas amostras sao sobre as mesmas pessoas.

foi feito um loop para fazer a diferença das notas entre as amostras: subtraçao = [b - a for a, b in zip(antes_treinamento, depois_treinamento)]

importando o test t pareado: from scipy.stats import ttest_rel
Aplicando o teste: ttest_rel(depois_treinamento, antes_treinamentom, alternative = 'greater') -> (para este caso a H1 era maioridade), e tambem retorna stats e p_valor
Para o t test pareadas se utiliza a lista com os valore e nao a media dos valores

No exemplo do curso foi obtido um valor_p bem pequeno (0.0006) o que indica que houve diferença apos o treinamento e podemos rejeitar o H0
"""

#A depender da H1 se só queremos saber se é diferente sem se importar com a direcao, chamamo de bilateral, e nao é necessario passar o parametro alternative




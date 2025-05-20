import pandas as pd
from scipy import stats
import numpy as np
"""
Partindo para o proxima parte do curso, onde será testado propriamente dito uma hipotese.
'A duracao media das lampadas de natal é de 1570h' -> Hipotese / Necessariamente precisa ser uma igualdade
A hipotese também é chamada de hipotese nula, e precisamos transformar ela em uma meétrica

H0: μ = 1570 -> normalmente nao se utiliza a letra grega mi(μ) para representar a media

Existe também a hipotese alternativa que é uma ideia que desafia a hipotese nula
H1: μ != 1570 -> hipotese alternativa

Com isso formulado temos o par de hipotese e esse é o objetivo de analise, com duas possibilidades, rejeitar ou assumir a hipotese nula

Após isso é necessario calcular o intervalo de confianca
"""

lampadas_natalinas = pd.read_csv('Conceitos/testando_hipoteses/experimento_lampadas_natalinas.csv')
media = lampadas_natalinas['duracao'].mean()

#Coletando o restante das informacoes necessarias
confianca = 0.95 #-> Nivel de confianca desejado
desvio_padrao_populacional = 105 #-> Valor passado pela fabricante
tamanho_amostra = len(lampadas_natalinas['duracao'])

print(f'Media amostral da lampada natalina: {media}')

#Calculando o Intervalo de confianca
IC = stats.norm.interval(confianca, loc=1570, scale= desvio_padrao_populacional/np.sqrt(tamanho_amostra))
print(f'IC (95%): {IC}') 

"""
Com base nessas informacoes mostradas devemos rejeitar a hipotese nula -> H0

Temos uma porcentagem que é chamada de nivel de significancia que é o restante do valor de confianca para 100 entao neste caso
nivel de significancia = 0.05 (5%) -> Que também representa a probabilidade de rejeitarmos a H0 e na verdade ela ser verdadeira

Existem dois tipos de erro são eles:
Tipo 1: ocorre quando a hipótese nula é rejeitada quando, na verdade, ela é verdadeira.
Tipo 2: ocorre quando a hipótese nula não é rejeitada quando, na verdade, ela é falsa.

--------------------------
Para calcular a probabilidade de observarmos a media amostral que observamos terá que ser realizado o teste Z
Teste Z -> from statsmodels.stats.weightstats import ztest -> os parametros necessarios são x1->amostra observada, value-> media estabelecida no H0, alternative-> tipo da H1 
"""
from statsmodels.stats.weightstats import ztest

#Executando o ztest
stats, p_valor = ztest(x1=lampadas_natalinas['duracao'], value = 1570, alternative = 'two-sided') #-> retorna estatistica do teste e o p valor que é a propabilidade de analisarmos exatamente essa amostra

print(p_valor).round(6) #-> abaixo de 0% ou seja mais um motivo para recursarmos a H0 pois a chance de observar esse media (1529) e baixa e mesmo assim foi observado
#Normalmente se compara o pvalor com o nivel de confianca que neste caso é 0.05 caso o pvalor seja maior podemos nao rejeitar a H0 mas se for menor rejeitamos

"""
Para utilizar o Teste Z é necessario algumas situacoes espcificas
1 - Tamanho da amostra é grande: Geralmente, o teste Z é usado quando o tamanho da amostra (n) é maior que 30. Isso se deve ao Teorema Central do Limite, que afirma que, para tamanhos de amostra suficientemente grandes
2 - Desvio padrão populacional é conhecido: Para aplicar o teste Z, você precisa conhecer o desvio padrão da população. Isso raramente acontece na prática, mas quando conhecido, permite o uso do teste Z para avaliar diferenças entre médias ou proporções.
3 - A amostra é aleatória e as observações são independentes: Isso garante que os dados não sejam enviesados e que o modelo estatístico aplicado seja válido.
"""
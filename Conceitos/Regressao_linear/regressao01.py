import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from statsmodels.formula.api import ols
from sklearn.metrics import r2_score
import statsmodels.api as sm

dados_casas = pd.read_csv('Conceitos\Regressao_linear\dados\Preços_de_casas.csv')
# print(dados_casas.info())

#Drpopou colunas irrelevantes para a regressao
dados_casas = dados_casas.drop(columns = 'Id')

#Correlacao - para analisar a correlacao de dois dados diferentes
corr = dados_casas.corr()
# print(corr['area_primeiro_andar']) #-> aqui vai retornar o valor de correlacao com o restante das colunas

#Devemos interpretar a intensidade e direcao:
#-1: Correlacao positiva perfeita: a medida que uma variavel aumenta a outra tambem aumenta
# 0: nao ha correlacao linear entre as variaveis
# 1: Correlacao negativa perfeita: a medida que uma variavel aumenta a outra tambem diminui


#Criando a correlacao em reta da area do primeiro andar com o preço do imovel:
#primeiro grafico de dispersão:
plt.scatter(dados_casas['area_primeiro_andar'], dados_casas['preco_de_venda'])
#Quero passar uma reta no grafico para mostrar a tendencia
plt.axline(xy1=(66,250000),xy2=(190,1800000), color='red')
plt.title('Relacao entre preco x area')
plt.xlabel('area da casa')
plt.ylabel('preco imovel')
# plt.show()


#Separando em entre treino e teste utilizando o sklearn
y = dados_casas['preco_de_venda']
x = dados_casas.drop(columns = 'preco_de_venda')
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state = 230) #Necessario para realizar a gerenalizacao

#Separando dados de treino para utilizar como parametro
df_treino = pd.DataFrame(data=x_treino)
df_treino['preco_de_venda'] = y_treino 

#Utilizando o OLS
modelo_0 = ols('preco_de_venda ~ area_primeiro_andar', data=df_treino).fit() #-> Treinando o modelo e o primeiro parametro é referente a relacao entre variaveis
print(modelo_0.params)
#.params retorna dois valores, o intercept e o area do primeiro andar, neste caso, e para interpretar este valor:
#Intercept: caso area do primeio andar seja zero, esse sera o valor da casa
#area_primeiro_andar: a cada metro quadrado o valor acrescentado sera o dito na variavel

#Coeficiente de determinaçao
#Valor de R²(CD) -> porcentagem de valores que a variavel explicativa consegue explicar
print(modelo_0.rsquared) #-> Neste caso aproximadamente 37% dos valores das casas é explicado pela area do primeiro andar

#Definindo o Y_previsto, utilizando o y_teste
y_predict = modelo_0.predict(x_teste)
print(r2_score(y_teste, y_predict)) #espera valor proximo do valor de r² dos dados que utilizamos no treino

#Para visualizar mais de uma variavel explicativa para o preco de venda por exemplo, podemos utilizar do pairplot
sns.pairplot(dados_casas, y_vars = 'preco_de_venda', x_vars = ['area_primeiro_andar', 'quantidade_banheiros'])
# plt.show()

#Adicionando variaveis ao modelo
x_train = sm.add_constant(x_treino)

#Criando o modelo de regressao linear saturado
modelo_1 = sm.OLS(y_treino, x_train[['const','area_primeiro_andar', 'existe_segundo_andar','quantidade_banheiros','qualidade_da_cozinha_Excelente']]).fit()

x_teste = sm.add_constant(x_teste) #Adicionando a coluna de constante ao conjunto de teste

#testando o modelo_1
predict_1 = modelo_1.predict(x_teste[['const','area_primeiro_andar', 'existe_segundo_andar','quantidade_banheiros','qualidade_da_cozinha_Excelente']])#Necessario filtrar apenas as colunas existentes no modelo utilizado

#Comparando os r² para checar se o modelo está generalista
print(f'R² Modelo: {modelo_1.rsquared}')
print(f'R² com o teste: {r2_score(y_teste, predict_1)}')

novo_imovel = pd.DataFrame({ 'const' : [1],
                            'area_primeiro_andar' : [120],
                            'existe_segundo_andar' : [1],
                            'quantidade_banheiros' : [2],
                            'qualidade_da_cozinha_Excelente' : [0]

})

#Prevendo o valor 
print(modelo_1.predict(novo_imovel)[0]) #posicao 0 apenas para nao truncar o valor
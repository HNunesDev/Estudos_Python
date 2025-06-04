import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from prophet.plot import plot_plotly

df = pd.read_csv('https://raw.githubusercontent.com/alura-cursos/data_science_projeto/refs/heads/main/Dados/bicicletas.csv')

# print(df.head())

""""
Exemplos descritos neste modulo serao baseados na aula do curso:
prever quantidade de alugueis de biciletas de uma emresa x a qual estamos prestando servicos
"""
# print(df.isnull().sum())
#Para tratar esses dados nulos sera utilizado o interpolate que tira a media do valor posterior e anterior

df['temperatura'] = df['temperatura'].interpolate(method='linear')
df['sensacao_termica'] = df['sensacao_termica'].interpolate(method = 'linear')

print(df.duplicated().sum())
#Existem linhas duplicadas, e é preciso tratar

df_limpo = df.drop_duplicates()
print(df_limpo.duplicated().sum())
# print(df.head())

#Proximo passo seria uma analise descritiva dos dados, de primeiro modo uma analise mais geral podemos utilizar a funcao describe
# print(df_limpo.describe())
#Posteriormente é bom checar como os dados estãos dispostos
fig, axs = plt.subplots(2,2, figsize=(16,5), sharey=True) 
axs[0,0].hist(
    x = df_limpo['temperatura'],
    bins = 10,
    edgecolor='black'
)
axs[0,1].hist(
    x= df_limpo['sensacao_termica'],
    bins = 10,
    edgecolor='black'
)
axs[1,0].hist(
    x=df_limpo['umidade'],
    bins= 10,
    edgecolor='black'
)

axs[1,1].hist(
    x=df_limpo['velocidade_vento'],
    bins=10,
    edgecolor='black'
)

axs[0,0].title.set_text('Temperatura')
axs[0,1].title.set_text('Sensacao termica')
axs[1,0].title.set_text('Umidade')
axs[1,1].title.set_text('Velocidade do vento')

# plt.show()

#Quando o padrao está diferente da distribuição normal, dizemos que ele está distorcido ou para esquerda ou para direita
#Checando a correlacao das colunas x contagem - variaveis numericas
df_correlacao = df_limpo.loc[:, ['temperatura', 'sensacao_termica', 'umidade', 'velocidade_vento', 'contagem']]
correlacao = df_correlacao.corr()
# print(correlacao)

#agora a correlacao com as variaveis categoricas
print(df_limpo.describe(include = [object])) #top é referente a moda e freq é valor da moda

#fazendo um looping para checar os valores unicos das colunas categorias
for col in ['clima',  'feriado', 'fim_de_semana', 'estacao']:
    print(f'Coluna: {col}')
    print(df_limpo[col].unique())
    print('='*25)

#Para saber a mediana no fim de semana. | Muito bom para saber a mediana das alternativas, independente da coluna categorica
mediana_fim_de_semana = df_limpo.groupby('fim_de_semana')['contagem'].median()
print(mediana_fim_de_semana)

#analise sobre o clima
df_clima = df_limpo.groupby('clima')['contagem'].sum().reset_index().sort_values(by='contagem', ascending = False)
plt.figure(figsize=(6,4))
sns.barplot(data=df_clima, y='clima', x='contagem', hue='clima', orient='h')
plt.title('Bicicletas alugadas por clima')
plt.xlabel('Contagem')
plt.ylabel('')
# plt.show()

print(df_limpo.groupby('estacao')['contagem'].mean())
#Para este caso será realizado o teste de hipotese de valores referente a outono e primaveia onde H0: = \ H1: !=
from scipy.stats import mannwhitneyu 

primavera = df_limpo[df_limpo['estacao'] == 'Primavera']['contagem']
outono = df_limpo[df_limpo['estacao'] == 'Outono']['contagem']

stats, p_valor = mannwhitneyu(primavera, outono, alternative = 'two-sided')
print(stats)
print(p_valor) #Pvalor abaixo de 0.05 entao a H0 é descartada e confirmamos que a sao diferentes

#Tratando a data
#É preciso converter a coluna para datetime para que seja possivel manipula-la
df_data = df_limpo.copy()
df_data['data_hora'] = pd.to_datetime(df_data['data_hora'])

#Agora apos transformar podemos até mesmo criar outras colunas com base nessa coluna ja existente
df_data['mes'] = df_data['data_hora'].dt.month
df_data['horario'] = df_data['data_hora'].dt.hour
df_data['data_hora'] = df_data['data_hora'].dt.date
df_data = df_data.rename(columns={
    'data_hora' : 'data'
})
df_data['data'] = pd.to_datetime(df_data['data'])
#Apos alterar a coluna data_hora ele retornou a ser um objeto, deve alterar novamente

# ============================================ previsao
#Para as previsoes utilizaremos a biblioteca prophet
from prophet import Prophet #Prophet é um modelo de regressao aditivo
#No curso foi dito que é preciso ter um Dataframe com apenas duas colunas, as datas e a quantidade de bicicleta, entao deve montar o df
df_prophet = df_data[['data', 'contagem']].rename(columns={
    'data': 'ds',
    'contagem' : 'y'
}) #É preciso renomear as colunas, o prophet reconhece a data com nome de ds e o que vai ser previsto y
#Por ter retirado o horario acabou que as datas ficam se repetindo, mas para isso vamos agrupar as datas e somar as contagens do dia

df_prophet = df_prophet.groupby('ds')['y'].sum().reset_index()
print(df_prophet.head())

#Aplicando o numero de seed para garantir a replicabilidade dos resultados
np.random.seed(4587)
modelo = Prophet()
modelo.fit(df_prophet) #Treinando o modelo criado

#Criando df para realizar a previsao
futuro = modelo.make_future_dataframe(periods = 90, freq='D')
previsao = modelo.predict(futuro)

#Visualizando a previsao
fig1 = modelo.plot(previsao) #Explicando esse grafico - o azul é a previsao de y, o preto é o valor real de y, e o azul mais claro é o intervalo de confianca, os traços azuis sem a presença das bolinhas retrata a previsao
# plt.show()
print(previsao[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]) #y_hat é o valor de yhat que foi previsto, os valores de yhat superior e inferior sao os valores do intervalo de confianca

fig2 = modelo.plot_components(previsao) #sao os componentes que o modelo utilizoiu pra fazer a previsao
#Tendencia
#sazonalidade - semanal e anual
# plt.show()

#====================================
#a Métrica responsavel para avaliarmos o modelo é o MSE que é basicamente a diferença do y previsto pelo y real ao quadrado, mais a somatoria dos valores de y dividide por n de y
#Mas isso daria um numero muito grande, entao para melhorar a visualizacao utilizamos o RMSE que é basicamente tirar a raiz quadrada do valor obtido do MSE
from sklearn.metrics import mean_squared_error

#mse = mean_squared_error(df_comparacao['y'], df_comparacao['yhat']) apenas um exemplo de usuabilidade df_comparacao = df com o valor previsto e o valor real de y
#rmse = np.sqrt(mse)

df_treino = pd.DataFrame()
# Separando 80% dos dados para treino
df_treino['ds'] = df_prophet['ds'][:584] #
df_treino['y'] = df_prophet['y'][:584]

df_teste = pd.DataFrame()

# Separando 20% dos dados para teste
df_teste['ds'] = df_prophet['ds'][584:]
df_teste['y'] = df_prophet['y'][584:]

modelo2 = Prophet(yearly_seasonality = True)
modelo2.fit(df_treino)
futuro = modelo.make_future_dataframe(periods=150, freq='D')
previsao = modelo.predict(futuro)

#Plotando agora que declaramos para o modelo que existe uma sazonalidade anual
fig3 = modelo.plot(previsao)
plt.plot(df_teste['ds'],df_teste['y'], '.r')
# plt.show()

#Calculando o RMSE
df_previsao = previsao[['ds', 'yhat']]
df_comparacao = pd.merge(df_previsao, df_teste, on = 'ds')

mse = mean_squared_error(df_comparacao['y'], df_comparacao['yhat'])
rmse = np.sqrt(mse)
print(f'Valor do mse: {mse} Valor do rmse: {rmse}')
#O valor do RMSE foi de aproximadamente 5k queremos melhorar esse resultado entao para isso vamos tratar os outliers
#OBS nem sempre o melhor a se fazer é retirar os outliers, mas neste caso é valido

#Removendo as linhas do df que estejam fora do intervalor de confianca
#Para isso vamos obter o intervalor de confianca
modelo_confianca = Prophet()
modelo_confianca.fit(df_prophet)
futuro = modelo.make_future_dataframe(periods = 0)
previsao = modelo.predict(futuro)
sem_outliers = df_prophet[(df_prophet['y'] > previsao[('yhat_lower')]) & (df_prophet['y'] < previsao['yhat_upper'])]

print(df_prophet.shape)
print(sem_outliers.shape) #Foi retirado 95 outiliers

df_treino = pd.DataFrame()

df_treino['ds'] = sem_outliers['ds'][:505]
df_treino['y'] = sem_outliers['y'][:505]

df_teste = pd.DataFrame()

df_teste['ds'] = sem_outliers['ds'][505:]
df_teste['y'] = sem_outliers['y'][505:]

modelo_semoutilier = Prophet(yearly_seasonality = True)
modelo_semoutilier.fit(df_treino)
futuro = modelo_semoutilier.make_future_dataframe(periods = 365, freq='D')
previsao = modelo_semoutilier.predict(futuro)

fig_sem = modelo_semoutilier.plot(previsao)
plt.plot(df_teste['ds'], df_teste['y'], '.r')
plt.show()

#tirando o RMSE do novo modelo sem outliers
df_previsao_sem = previsao[['ds', 'yhat']]
df_comparacao_sem = pd.merge(df_previsao_sem, df_teste, on = 'ds')
mse = mean_squared_error(df_comparacao_sem['y'], df_comparacao_sem['yhat'])
rmse = np.sqrt(mse)

print(f'MSE: {mse} RMSE: {rmse}')

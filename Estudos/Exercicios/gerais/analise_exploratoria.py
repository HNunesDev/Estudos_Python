import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = pd.read_csv('C:\\Users\\henri\\Downloads\\dados_covid.csv')
# print(dados.head())

#Verificando as colunas
# 'Unnamed: 0', 'status', 'origem', 'MS', 'data_boletim', 'data_coleta','state', 'data_dados', 'confirmed', 'deaths', 'vaccination', 'date_br','boletim_de_hoje', 'dados_de_hoje', 'UF', 'link_painel',
# 'frequencia_prints', 'obs_do_link'

#Para ordenar os estaod pela quantidade de mortes para mais tarde apssar como argumento para ordenar o gráfico
ordem_morte = dados.groupby('state')['deaths'].sum().sort_values(ascending=False).index

#Verificando possiveis casos de graficos
total_mortes = dados['deaths'].sum()
total_mortes_fora_sp = dados[dados['state'] != 'SP']['deaths'].sum()
total_mortes_sp = dados.loc[dados['state'] == 'SP', 'deaths'].sum()

total_sudeste = dados[dados['state'].isin(['SP', 'RJ', 'MG', 'ES'])]['deaths'].sum()
total_sul = dados[dados['state'].isin(['PR', 'SC', 'RS'])]['deaths'].sum()

df_suldeste_sul = {
    'regiao' : ['Sudeste', 'Sul'],
    'mortes' : [total_sudeste, total_sul]
}

df_comparacao = {
    'local' : ['SP', 'Outros estados'],
    'total_mortes' : [total_mortes_sp, total_mortes_fora_sp]
}
df_comparacao = pd.DataFrame(df_comparacao)

#Grafico de comparacao entre estados
sns.barplot(x='state', y='deaths', data=dados, order=ordem_morte, palette='dark:salmon')
plt.xlabel('Estados')
plt.ylabel('Numero de mortes')
plt.title('Mortes por estado - COVID')

#Grafico de comparação entre SP e os outros estados
# sns.barplot(x='local', y='total_mortes', data=df_comparacao, palette='dark:salmon')
# plt.title('Mortes dos estados em comparacao a SP - COVID')

#Grafico de comparacao entre sudeste e sul
# sns.barplot(x='regiao', y = 'mortes', data=df_suldeste_sul, palette='dark:salmon')
# plt.title('Mortes regioes Sudeste / Sul - COVID')

sns.despine()
plt.show()

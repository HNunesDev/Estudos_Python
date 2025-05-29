import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
plt.show()
import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/apartamentos_aluguel.csv'

df = pd.read_csv(url, sep=',')

#Colunas 'Quartos', 'Banheiros', 'Suites', 'Vagas', 'Elevador', 'Mobiliado', 'Piscina', 'Regiao', 'Ano', 'Valor'

#primeiro exercicio
# Sua missão nesta atividade é aplicar o método groupby() para agrupar os dados por região e utilizar o método describe() para obter estatísticas descritivas do valor do aluguel. As estatísticas descritivas fornecerão insights importantes como média, mediana, valor mínimo, máximo e quartis, oferecendo uma visão detalhada sobre a distribuição dos preços de aluguel em cada região.
df_aluguel = df.groupby('Regiao')['Valor'].describe()
# print(df_aluguel)

#Segundo exercicio
# Agrupe os dados por região e piscina e calcule a média dos preços de aluguel. Esta abordagem mostrará como as piscinas afetam os preços de aluguel em diferentes áreas da cidade.
df_piscina = df.groupby(['Regiao', 'Piscina'])['Valor'].mean().unstack().round(2)
# print(df_piscina)

#Terceiro exercicio
# Agrupe os dados pelo ano do imóvel e calcule a média do valor de aluguel para cada ano. Isso permitirá que você visualize a variação dos preços de aluguel ao longo do tempo e identifique padrões de aumento, estabilidade ou diminuição.
df_ano = df.groupby('Ano')['Valor'].mean().round(2)
print(df_ano)
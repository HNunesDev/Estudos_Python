import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/dados_automoveis.csv'
df = pd.read_csv(url, sep=',')
# Columns 'Marca', 'Modelo', 'Ano', 'Tipo_combustivel', 'Potencia_motor','Cilindros_motor', 'Tipo_transmissao', 'Rodas_motrizes','Numero_portas', 'Tamanho', 'Estilo', 'Consumo_estrada_milhas','Consumo_cidade_milhas', 'Valor($)'

#Primeiro exercicio
pivot_valor = pd.pivot_table(df, index='Estilo', values='Valor($)').sort_values(by='Valor($)', ascending=False).round(2)
# print(pivot_valor)

#Segundo exercicio
pivot_transmissao = pd.pivot_table(df, index='Tipo_transmissao', values='Valor($)').sort_values(by='Valor($)', ascending=False).round(2)
# print(pivot_transmissao)

#Terceiro exercicio
pivot_ano = pd.pivot_table(df, index='Ano', values='Valor($)', aggfunc=['mean', 'max', 'min']).round(2)
# print(pivot_ano)

#Quarto exercicio
pivot_tamanho = pd.pivot_table(df, index='Estilo', values='Valor($)', columns='Tamanho', fill_value=0).round(2)
print(pivot_tamanho)
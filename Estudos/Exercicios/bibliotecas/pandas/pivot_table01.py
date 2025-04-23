import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/loja_vendas.csv'

df = pd.read_csv(url, sep=',')
# Columns 'ID_compra', 'unidade', 'cidade', 'data', 'horario','categoria_produto', 'valor_unitario', 'quantidade', 'valor_total','metodo_pagamento', 'ID_cliente', 'programa_cashback', 'idade','avaliacao_compra']

#Primeiro exercicio
pivot_idade = pd.pivot_table(df, index='metodo_pagamento', values='idade').round(2).sort_values(by='idade', ascending=False)
# print(pivot_idade)

#Segundo exercicio
pivot_vendas = pd.pivot_table(df, index='categoria_produto', values='valor_total', aggfunc='sum').sort_values(by='valor_total', ascending=False)
# print(pivot_vendas)

#Terceiro exercicio
#Utilize o método pivot_table() para criar uma tabela que cruze as informações de unidade e categoria de produto, com o objetivo de calcular a soma do valor total de vendas para cada combinação de unidade e categoria.
pivot_unidade = pd.pivot_table(df, index='unidade', columns='categoria_produto', values='valor_total', aggfunc='sum')
# print(pivot_unidade)

#Quarto exercicio
#incluir uma coluna que sumarize o valor total de vendas para cada unidade e adicionar uma linha ao final da tabela que mostre o total de vendas para cada categoria
pivot_unidade2 = pd.pivot_table(df, index='unidade', columns='categoria_produto', values='valor_total', aggfunc='sum', margins=True, margins_name='Total')
# print(pivot_unidade2)
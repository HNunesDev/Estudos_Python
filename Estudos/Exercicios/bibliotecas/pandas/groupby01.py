import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/loja_vendas.csv'

df = pd.read_csv(url, sep=',')
# print(df.columns)
# Colunas: ID_compra,unidade,cidade,data,horario,categoria_produto,valor_unitario,quantidade,valor_total,metodo_pagamento,ID_cliente,programa_cashback,idade,avaliacao_compra

#Primeio exercicio
# Sua missão nesta atividade é carregar os dados de vendas, examinar as informações disponíveis, e aplicar o método groupby() para agrupar e sumarizar o valor total de vendas por unidade.
df_total_vendas = df.groupby('unidade')['valor_total'].sum().sort_values(ascending=False).reset_index()
# print(df_total_vendas)

#Segundo exercicio
# Sua missão nesta atividade é aplicar o método groupby() para agrupar e sumarizar o valor total de vendas por categoria de produto. Para tornar os resultados ainda mais claros, ordene as categorias de acordo com o valor total de vendas, do maior para o menor.
df_valor_categoria = df.groupby('categoria_produto')['valor_total'].sum().sort_values(ascending=False).reset_index()
# print(df_valor_categoria)

#Terceiro exercicio
# Sua missão nesta atividade é aplicar o método groupby() para agrupar os compradores por método de pagamento e calcular os valores mínimos, médios e máximos da idade dos compradores para cada método.
df_pagamento_idade = df.groupby('metodo_pagamento')['idade'].agg(['min', 'mean', 'max']).round()
print(df_pagamento_idade)
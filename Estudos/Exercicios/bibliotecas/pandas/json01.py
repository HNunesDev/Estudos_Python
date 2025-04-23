import pandas as pd
import json

#Primeiro
# df = pd.read_json('C:\\Users\\henri\\Vscode\\Estudos\\Exercicios\\arquivos\\questao_1.json')
# print(df.head())

#Segundo
# df1 = pd.read_json('C:\\Users\\henri\\Vscode\\Estudos\\Exercicios\\arquivos\\questao_2_1.json')
# df2 = pd.read_json('C:\\Users\\henri\\Vscode\\Estudos\\Exercicios\\arquivos\\questao_2_2.json')

# print(df1.head())
# print('-' *200)
# print(df2.head())

#Terceiro dividindo coluna que possui dicionario em outras colunas
# with open('C:\\Users\\henri\\Vscode\\Estudos\\Exercicios\\arquivos\\questao_3.json', 'r') as arquivo:
#     dados = json.load(arquivo)
# print('-' *200)
# df3 = pd.json_normalize(dados)
# print(df3.head())

#Quarto estrutura aninhada de 3 níveis.
# with open('C:\\Users\\henri\\Vscode\\Estudos\\Exercicios\\arquivos\\questao_4.json', 'r') as arquivo:
#     dados = json.load(arquivo)
# print('-' *200)
# df4 = pd.json_normalize(dados)
# print(df4.head())

#Quinta utilizando outro separador para o aninhado
# with open('C:\\Users\\henri\\Vscode\\Estudos\\Exercicios\\arquivos\\questao_5.json', 'r') as arquivo:
#     dados = json.load(arquivo)
# print('-' *200)
# df5 = pd.json_normalize(dados, sep='_')
# print(df5.head())

#Sexta #Json normalize nao consegue normalizar coisas diferente de dicionario - para esses casos precisamos utilizar o record_path passando a chave na qual ele ira passar
#Caso tenha colunas fora do esquema para adiciona-las basta usar o parametor meta e passar a lista com as colunas faltantes
# with open('C:\\Users\\henri\\Vscode\\Estudos\\Exercicios\\arquivos\\questao_6.json', 'r') as arquivo:
#     dados = json.load(arquivo)
# df6 = pd.json_normalize(dados, record_path='lista_lojas')
# print(df6.head())

#Setimo Normlizando varias listas
# with open('C:\\Users\\henri\\Vscode\\Estudos\\Exercicios\\arquivos\\questao_7.json', 'r') as arquivo:
#     dados = json.load(arquivo)
# dfsudeste = pd.json_normalize(dados, record_path='lojas_sudeste')
# dfsul = pd.json_normalize(dados, record_path='lojas_sul')
# df7 = pd.concat([dfsudeste, dfsul], ignore_index=True)
# print(df7.head())

#Oitavo Normalizando Aqui como o arquivo esta dentro de um dicionario deve passar o nome da chave e depois qual lista aninhada tratar ex loja -> loja_norte
# with open('C:\\Users\\henri\\Vscode\\Estudos\\Exercicios\\arquivos\\questao_8.json', 'r') as arquivo:
#     dados = json.load(arquivo)
# dfnordeste = pd.json_normalize(dados, record_path=['lojas', 'lojas_nordeste'])
# dfnorte = pd.json_normalize(dados, record_path=['lojas', 'lojas_norte'])
# df8 = pd.concat([dfnordeste, dfnorte], ignore_index=True)
# print(df8.head())

#Nono Colunas faltantes, para esse caso devemos utilizar o meta ['colunas'] como parametro no normalize
# with open('C:\\Users\\henri\\Vscode\\Estudos\\Exercicios\\arquivos\\questao_9.json') as arquivo:
#     dados = json.load(arquivo)
# df9 = pd.json_normalize(dados, record_path='vendas', meta=['id_loja', 'nome_loja'])
# print(df9.head())

#Decimo
with open('C:\\Users\\henri\\Vscode\\Estudos\\Exercicios\\arquivos\\questao_10.json') as arquivo:
    dados = json.load(arquivo)
df_detalhes = pd.json_normalize(dados['dados'], record_path='detalhes', meta=['id_loja', 'nome_loja'])
df_vendas = pd.json_normalize(dados['dados'], record_path='vendas', meta=['id_loja', 'nome_loja'])
df10 = pd.merge(df_detalhes, df_vendas, on=['id_loja', 'nome_loja'])
print(df10.head())
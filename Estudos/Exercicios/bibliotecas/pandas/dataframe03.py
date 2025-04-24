import pandas as pd

dados = {
    'Pessoa': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eduarda', 'Felipe', 'Gabriela', 'Henrique'],
    'Peso': [50, 80, 70, 95, 60, 110, 45, 130],
    'Altura': [1.60, 1.75, 1.68, 1.80, 1.55, 1.90, 1.50, 1.85]
}
df_saude = pd.DataFrame(dados)

#Primeiro exercicio
def categotizar_imc(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc <= 24.9:
        return 'Peso normal'
    elif imc <= 29.9:
        return 'Sobrepeso'
    elif imc <= 34.9:
        return 'Obesidade grau 1'
    elif imc <= 39.9:
        return 'Obesidade grau 2'
    else:
        return 'Obesidade grau 3'

df_saude['IMC'] = df_saude['Peso'] / (df_saude['Altura'] ** 2)
df_saude['Categoria'] = df_saude['IMC'].apply(categotizar_imc)
print(df_saude)

#Segundo exercicio
dados = {
    'Pessoa': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eduarda', 'Felipe', 'Gabriela', 'Henrique'],
    'Ganhos': [5000, 4000, 3500, 6000, 2500, 7000, 3000, 4500],
    'Despesas': [3000, 2500, 2000, 5000, 2000, 6000, 2500, 4000]
}
df_financas = pd.DataFrame(dados)

df_financas['Economida(%)'] = df_financas.apply(lambda x: (x['Ganhos'] - x['Despesas']) / x['Ganhos'] * 100, axis=1).round(2)
print(df_financas)

#Terceiro exercicio
dados = {
    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Cadeira', 'Impressora', 'Pen Drive', 'Mesa'],
    'Estoque': [30, 150, 45, 20, 60, 10, 80, 50]
}
df_produtos = pd.DataFrame(dados)

df_produtos['EstoqueBaixo'] = df_produtos['Estoque'].apply(lambda x: 'Necessita Reposiçao' if x < 50 else 'Estoque Suficiente')
print(df_produtos)




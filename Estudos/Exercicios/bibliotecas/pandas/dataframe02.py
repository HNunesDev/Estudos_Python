import pandas as pd

dados = {
    'PedidoID': [101, 102, 103, 104, 105],
    'Cliente': ['Alice', 'Bruno', 'Carla', 'Daniel', 'Eduarda'],
    'ValorTotal': [150.00, 200.00, 300.00, 120.00, 500.00],
    'QuantidadeItens': [3, 4, 6, 2, 10]
}

df_vendas = pd.DataFrame(dados)

#Primeiro exercicio
df_vendas['TicketMedio'] = df_vendas['ValorTotal']/df_vendas['QuantidadeItens']
print(df_vendas)


#Segundo exercicio

dados = {
    'Aluno': ['Alice', 'Bruno', 'Carla', 'Daniel', 'Eduarda', 'Felipe', 'Gabriela', 'Henrique'],
    'NotaFinal': [95, 82, 67, 45, 78, 88, 50, 30]
}

# Criando o DataFrame
df_alunos = pd.DataFrame(dados)

def classifica_aluno(nota):
    if nota >= 90:
        return 'Excelente'
    elif nota >= 75:
        return 'Bom'
    elif nota >= 50:
        return 'Regular'
    else:
        return 'Insuficiente'

df_alunos['CategoriaDesempenho'] = df_alunos['NotaFinal'].apply(classifica_aluno)
print(df_alunos)


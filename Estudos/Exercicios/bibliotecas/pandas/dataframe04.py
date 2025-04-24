import pandas as pd

dados = {
    'Vendedor': ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eduarda', 'Felipe', 'Gabriela', 'Henrique'],
    'Meta': [20000, 15000, 18000, 25000, 12000, 30000, 10000, 22000],
    'Vendas': [22000, 14000, 19000, 24000, 13000, 28000, 9000, 23000],
    'Comissão (%)': [5, 4, 6, 5, 4, 7, 3, 6]
}
df_vendas = pd.DataFrame(dados)
df_vendas['Desempenho'] = df_vendas.apply(
    lambda x: 'Atingiu a Meta' if x['Vendas'] >= x['Meta'] else 'Não Atingiu',
    axis=1
)

# Criando a coluna 'Comissão Recebida' com base nas vendas e comissão (%)
df_vendas['Comissão Recebida'] = df_vendas.apply(
    lambda x: (x['Comissão (%)'] / 100) * x['Vendas'],
    axis=1
)

print(df_vendas)

#--------------------------------------------------------------------------------------------------------------

#Segundo exercicio
dados = {
    'Texto': [
        "Bom dia! ☀️ Começando mais uma semana produtiva!",
        "Novo produto chegando! 🎉 #novidade #lancamento",
        "Promoção relâmpago ⚡ Aproveitem! #promo #desconto",
        "Boa noite pessoal! 🌙 Até amanhã! #boanoite",
        "Dica do dia: 💡 Mantenha-se hidratado! #saude #bemestar"
    ],
    'Horário': ['07:30', '15:45', '12:20', '22:15', '10:00'],
    'Hashtags': ['', 'novidade,lancamento', 'promo,desconto', 'boanoite', 'saude,bemestar'],
    'Caracteres_Emoji': ['☀️', '🎉', '⚡', '🌙', '💡']
}

df_posts = pd.DataFrame(dados)

# Função para determinar período do dia
def get_periodo(horario):
    hora = int(horario.split(':')[0])
    if 0 <= hora < 6:
        return 'Madrugada'
    elif 6 <= hora < 12:
        return 'Manhã'
    elif 12 <= hora < 18:
        return 'Tarde'
    else:
        return 'Noite'

# Função para análise do conteúdo
def analisar_conteudo(row):
    num_hashtags = len([tag for tag in row['Hashtags'].split(',') if tag])
    num_emojis = len(row['Caracteres_Emoji'])
    comprimento_texto = len(row['Texto'])
    
    return {
        'num_hashtags': num_hashtags,
        'num_emojis': num_emojis,
        'comprimento_texto': comprimento_texto
    }

df_posts['Período_Dia'] = df_posts['Horário'].apply(get_periodo)
df_posts['Análise_Conteúdo'] = df_posts.apply(analisar_conteudo, axis=1)

print(df_posts)
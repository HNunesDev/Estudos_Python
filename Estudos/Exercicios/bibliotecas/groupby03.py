import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/python_dados/refs/heads/main/Dados/pacientes_doenca_cardiaca.csv'

df = pd.read_csv(url, sep=',')
#Columns 'Idade', 'Sexo_biologico', 'Tipo_dor', 'Pressao_arterial', 'Colesterol','Glicemia_jejum>120', 'Resultados_ECG', 'Frequencia_cardiaca_max',      'Dor_exercicio', 'Depressao_ST', 'Inclinacao_ST', 'Numero_vasos_fluro', 'Teste_cintilografia', 'Doenca_cardiaca'

#Primeiro exercicio
# O primeiro desafio com esses dados será agrupá-los com base na presença/ausência de doença cardíaca e sexo biológico, e calcular as idades mínima, média e máxima para cada grupo. Esta análise ajudará a identificar se há padrões visíveis que associam idade e sexo biológico à prevalência de doença cardíaca nestes dados.
df_doencas = df.groupby(['Doenca_cardiaca', 'Sexo_biologico'])['Idade'].agg(['min','mean','max']).unstack().round(2)
# print(df_doencas)

#Segundo exercicio
df_cariaco = df.groupby(['Doenca_cardiaca', 'Tipo_dor'])['Depressao_ST'].agg(['min','mean','max']).unstack().round(2)
#Agrupe os dados pela presença de doença cardíaca e tipo de dor no peito, e calcule a média do exame Depressão_ST para cada grupo. Utilize o método unstack() para transformar os dados agrupados em uma tabela mais legível, facilitando a comparação entre os diferentes grupos.
# print(df_cariaco)

#Terceiro exercicio
#Agrupe os dados por doença cardíaca e sexo biológico e aplique várias funções de agregação para calcular as médias das seguintes variáveis: idade, pressão arterial, colesterol, frequência cardíaca máxima, Depressão ST, Inclinação ST e número de vasos detectados por fluoroscopia.
#Renomeie as colunas resultantes para indicar que contêm as médias das variáveis.

df_agg = df.groupby(['Doenca_cardiaca', 'Sexo_biologico']).agg({'Idade':'mean', 'Pressao_arterial':'mean', 'Colesterol':'mean', 'Frequencia_cardiaca_max':'mean', 'Depressao_ST':'mean', 'Inclinacao_ST':'mean', 'Numero_vasos_fluro':'mean'}).round(2)
df_agregacoes_pacientes = df_agg.rename(columns={
    'Idade': 'Media_Idade',
    'Pressao_arterial': 'Media_Pressao_arterial',
    'Colesterol': 'Media_Colesterol',
    'Frequencia_cardiaca_max': 'Media_Frequencia_cardiaca_max',
    'Depressao_ST': 'Media_Depressao_ST',
    'Inclinacao_ST': 'Media_Inclinacao_ST',
    'Numero_vasos_fluro': 'Media_Numero_vasos_fluro'
})

print(df_agregacoes_pacientes)


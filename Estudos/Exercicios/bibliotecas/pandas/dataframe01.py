import pandas as pd

# Dados das plantas
dados = {
    'Especie': ['Mangifera indica', 'Eucalyptus globulus', 'Pinus elliottii', 'Anacardium occidentale',
                'Coffea arabica', 'Hevea brasiliensis', 'Carica papaya', 'Theobroma cacao',
                'Cocos nucifera', 'Bertholletia excelsa'],
    'Regiao': ['Norte', 'Sul', 'Leste', 'Norte', 'Sul', 'Oeste', 'Leste', 'Norte', 'Oeste', 'Norte'],
    'AlturaMedia': [15, 30, 25, 12, 3, 20, 5, 10, 18, 40]
}

# Criando o DataFrame
df_plantas = pd.DataFrame(dados)


#Primeiro exercicio
#Grupo 1 plantas pequenas
df_plantas_pequenas = df_plantas[df_plantas['AlturaMedia'] <= 15]

#Grupo 2 plantas grandes
df_plantas_grandes = df_plantas[df_plantas['AlturaMedia'] > 15]

somatoria_baixas = df_plantas_pequenas['AlturaMedia'].sum()
somatoria_altas = df_plantas_grandes['AlturaMedia'].sum()

print(f'Grupo: Plantas Baixas\nSoma da altura media das plantas: {somatoria_baixas}\n--------------------------------------------------------')
print(f'Grupo: Plantas Altas\nSoma da altura media das plantas: {somatoria_altas}\n--------------------------------------------------------')

#Segundo exercicio
df_plantas['GrandePorte'] = df_plantas['AlturaMedia'].apply(lambda x :'Sim'if x > 20 else 'Não')
print(df_plantas.head())

#Terceiro exercicio
df_plantas['IndiceAlturaRelativa'] = df_plantas['AlturaMedia'] / df_plantas['AlturaMedia'].max()
print(df_plantas[['Especie', 'AlturaMedia', 'IndiceAlturaRelativa']].head())
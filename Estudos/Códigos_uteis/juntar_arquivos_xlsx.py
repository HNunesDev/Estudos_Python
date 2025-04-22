import pandas as pd
import os

def juntar_arquivos_pasta(caminho_pasta):

    #Lista arquivos na pasta
    arquivos = os.listdir(caminho_pasta)

    lista_df = []

    #Carrega cada arquivo excel da pasta
    for arquivo in arquivos:
        caminho_arquivo = os.path.join(caminho_pasta, arquivo)
        #Carrega o excel para um dataframe e amazena na lista
        df = pd.read_excel(caminho_arquivo)
        lista_df.append(df)
    
    resultado = pd.concat(lista_df, ignore_index=True)

    #Salvando na mesma pasta
    resultado.to_excel(os.path.join(caminho_pasta, 'resultado.xlsx'), index=False)

    print("Arquivos reunidos com sucesso!")

#passar caminho da pasta desejada
caminnho_pasta = 'caminho/da/pasta'
juntar_arquivos_pasta(caminnho_pasta)

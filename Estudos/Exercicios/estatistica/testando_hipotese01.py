import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df_techtaste = pd.DataFrame({'avaliacoes': [38, 44, 33, 42, 47, 33, 36, 39, 42, 36, 39, 34, 42, 42, 36, 43, 31, 35, 36, 41, 42, 30, 25, 38, 47, 36, 32, 45, 44, 45, 37, 48, 37, 36, 44, 49, 31, 45, 45, 40, 36, 50, 38, 34, 36, 42, 46, 49, 36, 34, 38, 31, 53, 40, 57, 40, 36, 42, 26, 50, 32, 43, 35, 37, 42, 30, 36, 43, 40, 43, 44, 52, 37, 51, 35, 47, 40, 50, 37, 49]})

#Priemrios
desvio_padrao_amostral = df_techtaste['avaliacoes'].std()
print(f"Desvio padrão amostral: {desvio_padrao_amostral}")

#Segundo
erro_padrao_amostral = stats.sem(df_techtaste['avaliacoes'])
print(f"Erro padrão amostral: {erro_padrao_amostral}")

#Terceiro
#Plotando graficos para ver dispersao dos dados
plt.figure(figsize=(10, 5))
plt.subplot(1,2,1)
plt.hist(df_techtaste['avaliacoes'], bins=15, alpha=0.7, edgecolor='blue')
plt.subplot(122)
#Esse segundo facilita na visualizacao da dispersao
sns.kdeplot(df_techtaste['avaliacoes'], linewidth=2, fill= True)
# plt.show()

#4 pergunta: Sim

#Quinto
media_df = df_techtaste['avaliacoes'].mean()
confianca = 0.9
tamanho_amostra = len(df_techtaste['avaliacoes'])

#Sexto
intervalor_confianca = stats.norm.interval(confianca, loc = media_df, scale = desvio_padrao_amostral/np.sqrt(tamanho_amostra))
intervalor_confianca95 = stats.norm.interval(0.95, loc = media_df, scale = desvio_padrao_amostral/np.sqrt(tamanho_amostra))
print(f"Intervalo de confiança: {intervalor_confianca}")
print(f"Intervalo de confiança: {intervalor_confianca95}")

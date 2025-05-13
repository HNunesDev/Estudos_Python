import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Carregando os dados
dados = pd.read_excel('C:\\Users\\henri\\Downloads\\Ocorrencias_criminais.xlsx')
# print(dados.columns)
#Colunas: ['Natureza', 'Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho','Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro','Total'

# print(dados['Natureza'])

#Todos delitos cometidos no mes
roubo_janeiro = dados['Janeiro'].sum()
roubo_fevereiro = dados['Fevereiro'].sum()
roubo_fevereiro = dados['Marco'].sum()

# roubo_veiculo_janeiro = dados['Natureza == "ROUBO DE VEÍCULO"' and 'Janeiro'].sum()
roubo_veiculo_janeiro = dados[dados['Natureza'] == 'ROUBO DE VEÍCULO']['Janeiro'].sum()
roubo_veiculo_fevereiro = dados[dados['Natureza'] == 'ROUBO DE VEÍCULO']['Fevereiro'].sum()
roubo_veiculo_marco = dados[dados['Natureza'] == 'ROUBO DE VEÍCULO']['Marco'].sum()

print(roubo_veiculo_janeiro)
df = {
    'meses': ['Janeiro', 'Fevereiro', 'Marco'],
    'roubo_veiculo': [roubo_veiculo_janeiro, roubo_veiculo_fevereiro, roubo_veiculo_marco],
}
df = pd.DataFrame(df)

sns.set(style="whitegrid")
ax = sns.barplot(x='meses', y='roubo_veiculo', data=df)
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', 
                fontsize=12, color='black', 
                xytext=(0, 10), textcoords='offset points')
plt.title('Roubo de Veículo - Janeiro a Marco')
plt.xlabel('Meses')
plt.ylabel('Número de Crimes')
plt.tight_layout()
plt.show()


# print(roubo_janeiro)
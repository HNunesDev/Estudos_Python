import pandas as pd
from sklearn.model_selection import train_test_split
from statsmodels.formula.api import ols
from sklearn.metrics import r2_score

data = {
    "horas_estudo": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "nota_prova": [52, 55, 61, 63, 68, 70, 74, 79, 85, 88]
}

df_notas = pd.DataFrame(data)
x = df_notas['horas_estudo']
y = df_notas['nota_prova']

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.3)

df_treino = pd.DataFrame(data=x_treino)
df_treino['nota_prova'] = y_treino


modelo = ols('nota_prova ~ horas_estudo', data=df_treino).fit()
print(f'R²: {modelo.rsquared}')

#Testando o modelo
print('-'*80)

predicao = modelo.predict(x_teste)
print(f'R² da predicao: {r2_score(y_teste, predicao)}')

df_comparativo = pd.DataFrame({
    'predicao' : predicao,
    'resultado' : y_teste
})
print('-'*80)
#Comparando o coeficiente de determinacao
print('Comparativo: ')
print(df_comparativo)

import pandas as pd
from sklearn.model_selection import train_test_split
from statsmodels.formula.api import ols
from sklearn.metrics import r2_score
import statsmodels.api as sm

data = {
    "horas_estudo":     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "cafe_xicaras":     [0, 1, 1, 2, 2, 3, 3, 3, 4, 5],
    "horas_sono":       [8, 7.5, 7, 6.5, 6, 6, 5.5, 5, 4.5, 4],
    "nota_final":       [50, 53, 57, 60, 64, 68, 71, 75, 80, 85]
}

df_dados = pd.DataFrame(data)
x = df_dados[['horas_estudo', 'cafe_xicaras', 'horas_sono']] #neste caso é preciso passar uma lista dentro do parametro para ser aceito
y = df_dados['nota_final']

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3) #Por conta do split foi necessario resetar o index do df para que nao cause NaN
df_treino = pd.DataFrame(x_treino)
df_treino['nota_final'] = y_treino

#Adicao de constante
x_treino = sm.add_constant(x_treino)
x_teste = sm.add_constant(x_teste)
#Resetando indice para passar ao modelo
x_treino = x_treino.reset_index(drop=True)
y_treino = y_treino.reset_index(drop=True)
print(x_treino)

modelo_0 = sm.OLS(y_treino, x_treino).fit()
print(f'Coeficiente de determinacao: {modelo_0.rsquared}')

predicao = modelo_0.predict(x_teste).reset_index(drop=True)
y_teste = y_teste.reset_index(drop=True)

comparacao = pd.DataFrame({
    'predicao' : predicao,
    'real' : y_teste.reset_index(drop=True)
})

print(f'Comparacao: \n{comparacao}')
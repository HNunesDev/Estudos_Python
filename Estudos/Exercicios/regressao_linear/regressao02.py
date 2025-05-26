import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#Mesmo grupo de dados que o primeiro exercicio, mas desta vez utilizando o linear regression ao inves do OLS

data = {
    "horas_estudo": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "nota_prova": [52, 55, 61, 63, 68, 70, 74, 79, 85, 88]
}

df_notas = pd.DataFrame(data)
x = df_notas[['horas_estudo']]
y = df_notas['nota_prova']

x_treino, x_teste, y_treino, y_teste = train_test_split(x,y, test_size = 0.3)

modelo = LinearRegression()
modelo.fit(x_treino,y_treino)

predicao = modelo.predict(x_teste)
comparativo = pd.DataFrame({
    'predicao' : predicao,
    'valor real' : y_teste
})

print('Comparativo: ')
print(comparativo)

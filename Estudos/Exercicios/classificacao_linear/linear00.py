from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(46) 

#O X retorna as dimensoes do dado e o Y sera o rotulo "grupo 1 | grupo 2"
X, Y = make_classification(n_features = 2, n_redundant = 0, n_informative = 1,
                           n_clusters_per_class = 1)
print(X.shape) #Tras pares de coordenadas que definem pontos no espaço
print(Y.shape) #Tras a classificacao de acordo com o dado de X

# plt.scatter(X[:,0], X[:,1], marker = 'o', c=Y, edgecolor='k') #Podemos passar um vetor de classe 'c' 
p = X[10]
print(Y[10])
# plt.plot(p[0], p[1], marker='x', markersize = 20) #Plotando um valor para checar a classificacao do mesmo
# plt.show()

def plotmodel(w1, w2, b):
    plt.scatter(X[:,0], X[:,1], marker = 'o', c=Y, edgecolor='k')

    xmin, xmax = plt.gca().get_xlim()
    ymin, ymax = plt.gca().get_ylim()


    x = np.linspace(-2, 4, 50)
    y = (w1*x - b)/2

    plt.axvline(0, -1, 1, color='k', linewidth = 1)
    plt.axhline(0, -2, 4, color='k', linewidth = 1)
    plt.plot(x,y)
    plt.grid(True)
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)
    plt.show()

w1 = 5
w2 = 1
b = -0.4
# plotmodel(w1, w2, b)


def classify(ponto, w1, w2, b):
    ret = w1*ponto[0] + w2*ponto[1] + b

    if ret >= 0:
        return 1, 'yellow'
    else:
        return 0, 'blue'
    
p = (2, -1)
classe, cor = classify(p, w1, w2, b)
print(classe, cor)

plotmodel(w1, w2, b)
plt.plot(p[0], p[1], marker='^', markersize = 30, color = cor) #Confirmando que a classificacao funcionou
# plt.show()

acertos = 0
for k in range(len(X)):
    categ, _ = classify(X[k], w1, w2, b)
    if categ == Y[k]:
        acertos +=1
print(f'Acuracia: {acertos}%')

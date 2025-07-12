import torch
from torch import nn

#Deve passar a dimensionalidade de features de entrada e saida

perceptron = nn.Linear(in_features=3, out_features=1)

#Duas formas de acessar os pesos e o vies
#1
for nome, tensor in perceptron.named_parameters():
    print(nome, tensor)
#2
print('')
print(perceptron.weight.data)
print(perceptron.bias.data)

#Pegando os pesos e bias
w1, w2, w3 = perceptron.weight.data.numpy()[0] #É preciso pegar apenas o primeiro elemento por conta da forma que ele é passado ao perceptron
b = perceptron.bias.data.numpy()

X = torch.Tensor([0, -1, 2])
Y = perceptron(X)
print(f'O valor do ponto é de: {Y}')
if Y >=0:
    print('Abaixo da camada')
else:
    print('Acima da camada')
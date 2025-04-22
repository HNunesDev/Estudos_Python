lista = []
lista_par = []
for i in range(10):
    n = int(input(f'Me passe dez valores e retornarei os numeros pares da lista {i}/10: '))
    lista.append(n)

for i in lista:
    if i % 2 == 0:
        lista_par.append(i)
print(f'A lista de numeros pares é: {lista_par}')
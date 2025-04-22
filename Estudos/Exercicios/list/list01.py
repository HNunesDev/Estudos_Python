# Primeiro exercicio
print('Entre com 6 valores e eu colocarei em uma lista')
lista : list[int] = []
while len(lista) < 6:
   num =  int(input(f'Entre com o valor {len(lista) +1}/6: '))
   lista.append(num)

print(f'Os valores que voce digitou foram: {lista}')

#Segundo exercicio
A = [1, 0, 5, -2, -5, 7]
soma = A[0] + A[1] + A[5]

A[5] = 100

for num in A:
    print(num)

# Terceiro exercicio 
print('Entre com 10 valores e eu colocarei em uma lista')
B : list[int] = []
while len(B) < 10:
    valor = (input(f'Informe o valor {len(B) + 1}/10: '))                        
    B.append(valor)

contagem=0
for num in range(len(B)):
    if int(B[num]) % 2 == 0:
        contagem = contagem+1

print(f'Existem {contagem} de numeros pares na lista')


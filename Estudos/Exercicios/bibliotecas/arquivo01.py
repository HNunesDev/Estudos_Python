import os
#Exercicio 1
'''
Crie um programa que.
a) Crie/abra um arquivo texto de nome “arq.txt”
b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário entre com o caractere
“0”.
c) Feche o arquivo
d) Abra, leia o arquivo e escreva na tela todos os caracteres armazenados
'''
with open('arq.txt', 'a') as arquivo:
    while True:
        caractere: str = input('Informe um caractere ou 0 para sair: ')

        if caractere != '0':
            arquivo.write(f'{caractere}\n')
        else:
            break

with open('arq.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

for i in linhas:
    print(i)

# os.remove('arq.txt')

#Exercicio 2
'''
Faça um programa que receba do usuário o nome de um arquivo texto e mostre na tela quantas letras são
vogais e quantas são consoantes.
'''
vogais = ['a', 'e', 'i', 'o', 'u']
nvogais = 0
nconso = 0
arq = input('Passe o nome do arquivo txt: ')

if os.path.exists(f'{arq}.txt'):
    with open(f'{arq}.txt', 'r') as arquivo2:
        for linha in arquivo2:
            for letra in linha.strip():
                if letra.isalpha():
                    if letra.lower() in vogais:
                        nvogais +=1
                    else:
                        nconso += 1

    print(f'A quantidade de vogais são: {nvogais}')
    print(f'A quantidade de consoantes são: {nconso}')
else:
    print('Arquivo nao encontrado')
# os.remove('arq.txt')

#Exercicio 3
'''
Faça um programa que receba do usuário o nome de um arquivo texto e mostre na tela quantas linhas este
arquivo possui.
'''
lenlinhas = 0
arq2 = input('Passe o nome do arquivo txt: ')
if os.path.exists(f'{arq2}.txt'):
    with open(f'{arq2}.txt', 'r') as arquvio3:
        for linha in arquvio3:
            lenlinhas += 1
    print(f'Existem {lenlinhas} linhas')
else:
    print('Arquivo nao encontrado')
os.remove('arq.txt')
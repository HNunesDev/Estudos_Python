atletas = [
    ["Maria Silva", 1.75, 65],
    ["João Santos", 1.80, 72],
    ["Ana Pereira", 1.68, 58],
    ["Pedro Oliveira", 1.92, 85],
    ["Carlos Lima", 1.85, 78],
    ["Beatriz Souza", 1.70, 60],
    ["Fernanda Costa", 1.62, 55],
    ["Lucas Almeida", 1.88, 82],
    ["Rafaela Gomes", 1.74, 63],
    ["Gustavo Ferreira", 1.90, 88],
    ["Larissa Rocha", 1.66, 57],
    ["Henrique Nunes", 1.83, 76],
    ["Juliana Martins", 1.72, 59],
    ["Ricardo Carvalho", 1.86, 80],
    ["Sofia Alves", 1.64, 54],
    ["Matheus Ribeiro", 1.89, 84],
    ["Camila Duarte", 1.69, 61],
    ["Gabriel Monteiro", 1.77, 73],
    ["Eduarda Farias", 1.71, 62],
    ["Thiago Mendes", 1.84, 79],
]


#Primeiro ---------------
# for pessoa in atletas:
#     print(f'Nome: {pessoa[0]}\nAltura: {pessoa[1]}\nPeso: {pessoa[2]}\n----------------')


#Segundo  ---------------
# altura_media = round(sum([pessoa[1] for pessoa in atletas]) / len(atletas), 2)
# print(altura_media)


#Terceiro ---------------
# atletas_sobrepeso = [atleta[0] for atleta in atletas if (atleta[2] / (atleta[1] ** 2)) > 25]
# print("Atletas com IMC maior que 25:")
# print(atletas_sobrepeso)


#Quarto ---------------
# Classificação dos atletas com base no IMC
classificacao_imc = [
    (atleta[0], "Sobrepeso" if (atleta[2] / (atleta[1] ** 2)) > 25 else "Peso Normal")
    for atleta in atletas
]
print("Classificação dos atletas:")
print(classificacao_imc)


usuarios = {
    "João": 25,
    "Maria": 17,
    "Ana": 19,
    "Carlos": 16,
    "Beatriz": 22,
    "Pedro": 15,
    "Luiza": 18
}

classificacao_usuarios = {
    nome: 'Maior' if idade >= 18 else 'Menor'
    for nome, idade in usuarios.items()
}
print(classificacao_usuarios)



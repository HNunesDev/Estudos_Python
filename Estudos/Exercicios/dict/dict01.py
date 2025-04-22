livros = [
    ("Dom Quixote", "Miguel de Cervantes", 1605),
    ("Orgulho e Preconceito", "Jane Austen", 1813),
    ("O Grande Gatsby", "F. Scott Fitzgerald", 1925),
    ("Cem Anos de Solidão", "Gabriel García Márquez", 1967),
    ("1984", "George Orwell", 1949),
    ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997),
    ("O Senhor dos Anéis", "J.R.R. Tolkien", 1954),
    ("A Revolução dos Bichos", "George Orwell", 1945),
    ("O Apanhador no Campo de Centeio", "J.D. Salinger", 1951),
    ("O Código Da Vinci", "Dan Brown", 2003),
]

#Primeiro
# classificacao_livos = [
#     (livro[0], 'Morderno' if livro[1] >= 2000 else 'Clássico')
#     for livro in livros
# ]
# print(classificacao_livos)

#Segundo
dict_livros = {
    livro[0]: {"autor": livro[1], 'ano': livro[2]}
    for livro in livros
}
# print(dict_livros)
# print('-' *20)
#Terceiro
# livros_antigos = {
#      livro[0]: livro[2] for livro in livros if livro[2] <= 1950
# }

# print(livros_antigos)

#Quarto
livros_atualizados = {
    livro[0]: {'autor' : {livro[1]}, 'ano' : (2025 - livro[2])} for livro in livros
}
print(livros_atualizados)
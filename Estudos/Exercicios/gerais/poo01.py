#Exercicio 1
# 1. Crie uma classe Pessoa, contendo nome, data de nascimento e email. Crie as propriedades getters e
# setters para os atributos e um método para imprimir os dados de uma pessoa.
from datetime import date

class Pessoa:

    def __init__(self, nome : str, dt_nascimento : date, email : str) -> None:
        self.__nome = nome
        self.__dt_nascimento = dt_nascimento
        self.__email = email

    @property
    def nome(self) -> str:
        return self.__nome  
    @nome.setter
    def nome(self, nome : str) -> None:
        self.__nome = nome

    @property
    def dt_nascimento(self) -> date:
        return self.__dt_nascimento
    @dt_nascimento.setter
    def dt_nascimento(self, dt_nascimento : date) -> None:
        self.__dt_nascimento = dt_nascimento

    @property
    def email(self) -> str:
        return self.__email
    @email.setter
    def email(self, email : str) -> None:
        self.__email = email
    
    def info_pessoa(self) -> None:
        return print(f'O(A) {self.nome}, nasceu em {self.dt_nascimento} e tem o email: {self.email}')
    
pessoa1 = Pessoa('Henrique', '13/03/2002', 'henriqueguilhem77@gmail.com')
pessoa1.info_pessoa()

#2. Crie uma classe Agenda que pode armazenar contatos e seja possível realizar as seguintes operações:
# a) armazenar_contato(contato: Contato);
# b) remover_contato(contato: Contato);
# c) buscar_contato(nome: str); // Informa em que posição da agenda está o contato.
# d) imprimir_agenda(); // Imprime os dados de todos os contatos da agenda.
# e) imprimir_contato(indice: int); // Imprime os dados do contato informado pelo índice.

class Contato:
    def __init__(self, nome: str, telefone: str):
        self.nome = nome
        self.telefone = telefone

    def __repr__(self):
        return f"Contato(Nome: {self.nome}, Telefone: {self.telefone})"


class Agenda:
    def __init__(self):
        self.contatos = []  # Lista para armazenar os contatos

    def armazenar_contato(self, contato: Contato):
        """Adiciona um contato à agenda."""
        self.contatos.append(contato)
        print(f"Contato {contato.nome} armazenado com sucesso!")

    def remover_contato(self, contato: Contato):
        """Remove um contato da agenda, se existir."""
        if contato in self.contatos:
            self.contatos.remove(contato)
            print(f"Contato {contato.nome} removido com sucesso!")
        else:
            print(f"Contato {contato.nome} não encontrado.")

    def listar_contatos(self):
        """Lista todos os contatos armazenados na agenda."""
        if self.contatos:
            print("\nLista de Contatos:")
            for contato in self.contatos:
                print(contato)
        else:
            print("A agenda está vazia.")


# Exemplo de uso:
agenda = Agenda()

# Criando contatos
contato1 = Contato("Henrique", "11-982022406")
contato2 = Contato("Jose", "11-999988777")

# Armazenando contatos
agenda.armazenar_contato(contato1)
agenda.armazenar_contato(contato2)

# Listando contatos
agenda.listar_contatos()

# Removendo um contato
agenda.remover_contato(contato2)

# Listando contatos novamente
agenda.listar_contatos()

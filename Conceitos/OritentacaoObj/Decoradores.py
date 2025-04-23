"""
Decoradores são funcoes de maior grandeza, é utilizado funcao como parametro
Envolvem funcoes e aprimoram seus comportamentos
Tem sua propria sintase utilizando "@"
Tem o intuito realmente de decorar no sentido de enfeitar
"""
#Ex
def seja_educado_mesmo(funcao):
    def educado():
        print('Foi um prazer conhecer voce')
        funcao()
        print('Tenha um excelente dia!')
    return educado

@seja_educado_mesmo #Aqui chamamos a funcao de decoraçao utilizando @ ao invez de passar a ela a funcao que quero como parametro
def apresentnado():
    print('Meu nome é Henrique')

apresentnado()
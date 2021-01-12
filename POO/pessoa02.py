"""
Associação - Usa outro objeto(classesTeste.py)
Agregação - Tem outro objeto(compras.py)
Composição - É dono de outro objeto(clientes.py)
Herança - É outro objeto(Este arquivo)

"""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_classe = self.__class__.__name__
        
    def falar(self):
        print(f'{self.nome_classe} falando...')
        
class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome_classe} comprando...')

class ClienteVIP(Cliente):
    #Sobreposição de métodos
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        print(f'{self.nome} {self.sobrenome}')
        
class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome_classe} estudando...')

c1 = ClienteVIP('jose', 18, 'Ferreira')
c1.falar()
    




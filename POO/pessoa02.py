"""
Associação - Usa outro objeto
Agregação - Tem outro objeto
Composição - É dono de outro objeto
Herança - É outro objeto

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
        
class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome_classe} estudando...')
    




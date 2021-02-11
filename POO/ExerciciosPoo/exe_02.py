from datetime import datetime

class Pessoa:
    ano = datetime.today().year
    
    def __init__(self, nome:str, ano_nascimento:int, peso:int, altura:float):
        self.nome = nome
        self.ano_nascimento = ano_nascimento
        self.peso = peso
        self.altura = altura
        
    def idade(self):
        idade = self.ano - self.ano_nascimento
        return idade
    
    def engordar(self, peso):
        self.peso += peso
        
    def emagrecer(self, peso):
        self.peso -= peso
        
    def crescer(self, altura):
        self.altura += altura
        
if __name__ == "__main__":
    p1 = Pessoa("Júnior", 2002, 90.8, 1.70)
    print(p1.idade())
        
        
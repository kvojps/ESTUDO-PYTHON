class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco -= self.preco * (percentual / 100)

    #Getter
    @property
    def preco(self):
        return self._preco
    #Setter
    @preco.setter
    def preco (self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor


p1 = Produto('Camiseta', 'R$50')
p1.desconto(10)
print(p1.preco)
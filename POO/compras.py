class CarrinhoDeCompra:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

#Exemplos de agregação: 

carrinho = CarrinhoDeCompra()
produto_1 = Produto('Curso', 100)
produto_2 = Produto('Camisa', 30)
produto_3 = Produto('Caneca', 20)

carrinho.inserir_produto(produto_1)
carrinho.inserir_produto(produto_2)
carrinho.inserir_produto(produto_3)

carrinho.listar_produtos()
print(carrinho.soma_total())
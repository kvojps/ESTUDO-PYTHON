"""
Em outras linguagens de programação:
- public : Atributo ou metodo disponivel dentro e fora da classe
- protected : Atributo ou metodo disponivel na classe mãe e suas filhas
- private : Atributo ou metodo disponivel apenas dentro da classe

Python:
- Privado menos seguro: _var
- Privado mais seguro: __var (Não pode ser alterado fora da classe)

"""
class BaseDeDados:
    def __init__(self):
        self.__dados = {}
    
    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id : nome}
        else :
            self.__dados['clientes'].update({id : nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_clientes(self, id):
        del self.__dados['clientes'][id]







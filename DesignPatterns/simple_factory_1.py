"""
Na POO, o termo factory refere-se a uma classe ou método que é responsável por criar objetos.
Permitem criar um sistema com baixo acoplamento entre classes porque ocultam as classes que criam os objetos do 
código do cliente.

- Facilitam a adição de novas classes ao código, porque o cliente não conhece e nem utiliza a implementação da classe.

- Podem introduzir muitas classes no código(desvantagem).
"""
from abc import ABC, abstractmethod
from random import   choice

class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass

class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo está buscando o cliente.')

class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de popular está buscando o cliente.')

# Trabalhando o conceito de simple factory.
# Simple factory pode não ser considerado um padrão de projeto por si só.
# Cria-se uma classe construtora para que derivados da classes veiculo não sejam mencionados diretamente no cliente.
 
class VeiculoFactory:
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        assert 0, 'Veículo não existe.'

if __name__ == "__main__":
    carros_disponiveis = ['luxo','popular']
    for i in range(10):
        carro = VeiculoFactory.get_carro(choice(carros_disponiveis))
        carro.buscar_cliente()


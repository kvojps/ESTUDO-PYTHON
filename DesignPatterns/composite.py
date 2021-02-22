"""
Composite é um padrão de projeto estrutural que permite que você utilize a composição
para criar objetos em estrutura de árvores. O padrão permite aos clientes tratarem de maneira
uniforme objetos individuais (Leaf) e composições de objeto (Composite).

--> Só aplique este padrão em uma estrutura que possa ser representada em formato hierárquico 
    (árvore).

Objetos Composite são objetos mais complexos e com filhos. Geralmente, eles delegam trabalho para os filhos 
usando um método em comum. Objetos Leaf são objetos simples, da ponta e sem filhos. Geralmente, são esses objetos 
que realizam o trabalho real da aplicação.

"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class BoxStructure(ABC):
    #Component
    @abstractmethod
    def print_content(self) -> None: pass

    @abstractmethod
    def get_price(self) -> float: pass

    def add(self, child: BoxStructure) -> None: pass
    
    def remove(self, child: BoxStructure) -> None: pass
         
class Box(BoxStructure):
    #Composite
    def __init__(self, name):
        self.name = name
        self._children: List[BoxStructure] = []

    def print_content(self) -> None:
        print(f'\n{self.name}:')
        for child in self._children:
            child.print_content()


    def get_price(self) -> float:
        return sum([
            child.get_price() for child in self._children
        ])

    def add(self, child: BoxStructure) -> None:
        self._children.append(child)
    
    def remove(self, child: BoxStructure) -> None:
        if child in self._children:
            self._children.remove(child)

class Product(BoxStructure):
    #Leaf
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_content(self) -> None:
        print(f'{self.name}: R${self.price}')

    def get_price(self) -> float:
        return self.price

if __name__ == "__main__":
    #LEAF
    camisa1 = Product("Camisa 1", 50)
    camisa2 = Product("Camisa 2", 40)
    camisa3 = Product("Camisa 3", 30)
    
    cell1 = Product("Celular 1", 1000)
    cell2 = Product("Celular 2", 500)

    #COMPOSITE
    caixa_camisa = Box('Caixa de camiseta')
    caixa_camisa.add(camisa1)
    caixa_camisa.add(camisa2)
    caixa_camisa.add(camisa3)

    caixa_celular = Box("Caixa de celular")
    caixa_celular.add(cell1)
    caixa_celular.add(cell2)

    caixa_produtos = Box("Embalagem")
    caixa_produtos.add(caixa_camisa)
    caixa_produtos.add(caixa_celular)
    caixa_produtos.print_content()
    print(caixa_produtos.get_price())
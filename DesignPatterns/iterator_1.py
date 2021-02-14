"""
Iterator é um padrão comportamental que tem a intenção de fornecer um meio de acessar
, sequencialmente, os elementos de um objeto agregado sem expor sua representação 
subjacente.

A ideia principal do padrão é retirar a responsabilidade  é retirar a responsabilidade 
de acesso e percurso de uma coleção, delegando tais tarefas para um objeto iterador.

"""
from abc import ABC, abstractmethod
from collections.abc import Iterator, Iterable
from typing import List, Any

class MyIterator(Iterator):
    def __init__(self, collection: List[Any]):
        self._collection = collection
        self._index = 0
        
    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration

class MyList(Iterable):
    def __init__(self):
        self._items : List[Any] = []
        
    def add(self, value: Any):
        self._items.append(value)
        
    def __iter__(self):
        return MyIterator(self._items)
    
    def __str__(self):
        return f'{self.__class__.__name__}({self._items})'
    
if __name__ == "__main__":
    mylist = MyList()
    mylist.add('Jose')
    mylist.add('Ferreira')
    mylist.add('Junior')
    mylist.add('Maria')
    for x in mylist:
        print(x)
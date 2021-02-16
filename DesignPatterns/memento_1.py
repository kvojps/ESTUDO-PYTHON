"""
Memento é um padrão de projeto comportamental que tem a intenção de permitir
que você salve e restaure(basicamente fazer um backup dos dados) um estado anterior de um objeto originator 
sem revelar os detalhes da sua implementação e sem violar o encapsulamento.

-> Originator é a classe que cria e restaura o seu própio estado.
-> Memento é uma classe imutável que armazena a cópia do estado do originator.
-> Caretaker é a classe que toma conta dos mementos do originator. 
"""
from __future__ import annotations
from typing import Dict, List
from copy import deepcopy


class Memento:
    def __init__(self, state: Dict) -> None:
        self._state : Dict
        super().__setattr__('_state', state)
        
    def get_state(self) -> Dict:
        return self._state
    
    def __setattr__(self, name, value):
        raise AttributeError('Esta classe é imutável')
    
#Originator    
class ImageEditor:
    def __init__(self, name:str, width:int, height:int) -> None:
        self.name = name
        self.width = width
        self.height = height
        
    def save_state(self) -> Memento:
        #Faz uma cópia dos atributos do init desta classe
        return Memento(deepcopy(self.__dict__))
    
    def restore(self,memento:Memento) -> None:
        self.__dict__ = memento.get_state()
        
    def __str__(self):
        return f'{self.__class__.__name__}({self.__dict__})'
    
class Caretaker:
    def __init__(self, originator: ImageEditor ):
            self._originator = originator
            self._mementos: List[Memento] = []
                       
    def backup(self) -> None:
        self._mementos.append(self._originator.save_state())
     
    def restore(self) -> None:
        if not self._mementos:
            return
        
        self._originator.restore(self._mementos.pop()) 
        
            
if __name__ == "__main__":
    img = ImageEditor('foto_1.jpg', 500, 500)
    
    #fazendo backup de img
    caretaker = Caretaker(img)
    caretaker.backup()
    
    img.name = 'foto_2.jpg'
    img.width = 250
    img.height = 250
    print(img)
    
    caretaker.restore()
    print(img)
    
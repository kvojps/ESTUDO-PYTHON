"""
Template method tem a intenção de definir um algoritmo  em um método, postergando alguns passos para as subclasses
por herança. Template method permite que subclasses redefinam certos passos de um algoritmo sem mudar a estrutura
do mesmo.

Também é possível definir hooks para que as subclasses utilizem caso necessário.

A classe abstrata é quem chamará os métodos criados pela classe concreta.
"""

from abc import ABC, abstractmethod

class Abstract(ABC):
    def template_method(self):
        self.hook()
        self.operation1()
        self.operation2()
    
    def hook(self):pass
    
    @abstractmethod
    def operation1(self):pass    
    
    @abstractmethod
    def operation2(self):pass    
    
class ConcretClass0(Abstract):
    def hook(self):
        print("Utilizando o Hook")
        
    def operation1(self):
        print("Operação 1 concluída")    
    
    def operation2(self):       
        print("Operação 2 concluída")  

class ConcretClass1(Abstract):
    def operation1(self):
        print("Operação 1 concluída de maneira diferente")    
    
    def operation2(self):       
        print("Operação 2 concluída de maneira diferente")  
        
if __name__ == "__main__":
    c1 = ConcretClass0()
    c1.template_method()  
   
    c2 = ConcretClass1()
    c2.template_method()  
    



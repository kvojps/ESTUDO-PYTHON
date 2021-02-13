from abc import ABC, abstractmethod

class Pizza(ABC):
    def prepare(self):
        #Template method
        self.add_ingredients()
        self.cook()
        self.cut()
        self.serve()
        
    @abstractmethod
    def add_ingredients(self):pass
    
    @abstractmethod
    def cook(self):pass
    
    def cut(self):
        print(f'{self.__class__.__name__}: Cortando a pizza !')
    
    def serve(self):
        print(f'{self.__class__.__name__}: Servindo a pizza !')
        
class PizzaFrango(Pizza):
    def add_ingredients(self):
        print('Pizza de frango: Frango'
            ' Queijo, Orégano.')
        
    def cook(self):
        print('Pizza de Frango: Pronta em 20 minutos no forno a 180 graus.')
        
if __name__ == "__main__":
    pizza = PizzaFrango()
    pizza.prepare()
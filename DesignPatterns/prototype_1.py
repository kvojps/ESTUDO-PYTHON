"""
Especificar os tipos de objetos a serem criados usando uma instância-protótipo e criar novos objetos pela cópia
desse protótipo.
"""
from typing import List

class StringReprMixin:
    def __str__(self):
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()

class Person(StringReprMixin):
    def __init__(self,firstname: str,lastname: str)-> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addresses : List[Address] = []

    def add__address(self, Address) -> None:
        self.addresses.append(Address)

class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number

if __name__ ==  "__main__":
    from copy import deepcopy

    jose = Person('Jose','Ferreira')
    endereco_jose = Address('Avenida do programador', 56)
    jose.add__address(endereco_jose)
    print(jose)
    maria = deepcopy(jose)
    maria.firstname = 'maria'
    print(maria)

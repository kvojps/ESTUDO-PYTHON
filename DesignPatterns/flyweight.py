"""
Flyweight é um padrão de projeto estrutural que tem a intenção de usar compartilhamento
para suportar eficientemente grandes quantidades de objetos de forma granular.

Só use o flyweight quando todas as condições a seguir forem verdadeiras:
- Uma aplicação utiliza uma grande quantidade de objetos.
- Os custos de armazenamento são altos devido a uma grande quantidade de objetos.
- A maioria dos estados de objetos podem se tornar extrínsecos.
- Muitos objetos podem ser substituídos por poucos objetos compartilhados.
- A aplicação não depende do estado dos objetos.

"""

from __future__ import annotations
from typing import List, Dict

class Client:
    def __init__(self, name: str):
        self.name = name 
        self._addresses: List = []

        #dados extrínsecos
        self.address_number: str
        self.address_details : str

    def add_address(self, address: Address):
        self._addresses.append(address)

    def list_address(self):
        for address in self._addresses:
            address.show_addres(self.address_number, self.address_details)

class Address:
    #Flyweight
    def __init__(self, street:str, neighbourhood:str, zip_code:str):
        self._street = street
        self._neighbourhood = neighbourhood
        self._zip_code = zip_code

    def show_addres(self, address_number, address_details):
        print(
            self._street , address_number, self._neighbourhood, address_details,
            self._zip_code 
        )

class AddressFactory:
    _addresses: Dict = {}

    def _get_key(self, **kwargs):
        return ''.join(kwargs.values())

    def get_address(self, **kwargs):
        key = self._get_key(**kwargs)

        try:
            address_flyweight = self._addresses[key]
            print('Usando objeto já criado')
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
            print('Criando novo objeto')

        return address_flyweight

if __name__ == "__main__":
    address_factory = AddressFactory()
    
    a1 = address_factory.get_address(
        street='Av prog', 
        neighbourhood='Centro',
        zip_code='111111111')

    a2 = address_factory.get_address(
        street='Av prog', 
        neighbourhood='Centro',
        zip_code='111111111')

    jose = Client('Jose')
    jose.address_number = '56'
    jose.address_details = 'casa'
    jose.add_address(a1)
    jose.list_address()
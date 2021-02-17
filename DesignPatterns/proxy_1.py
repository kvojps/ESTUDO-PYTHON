"""
O proxy é um padrão de projeto estrutural que tem a intenção de fornecer um objeto substituto que 
atua como se fosse o objeto real que o código cliente gostaria de usar.

-> Proxy Virtual: controla acesso a recursos que podem ser caros para criação ou utilização.
-> Proxy Remoto: controla acesso a recursos que estãoem servidores remotos.
-> Proxy de proteção: controla acesso a recursos quepossam necessitar autenticação ou permissão.
-> Proxy inteligente: além de controlar acesso aoobjeto real, também executa tarefas adicionais para
saber quando e como executar determinadas ações.
"""
from __future__ import annotations
from abc import ABC,abstractmethod
from time import sleep
from typing import List,Dict

class IUser(ABC):
    firstname: str
    lastname: str
    
    @abstractmethod
    def get_address(self):pass
    
    @abstractmethod
    def get_all_user_data(self) -> Dict:pass
    
class RealUser(IUser):
    def __init__(self, firstname:str, lastname:str):
        sleep(2) #Simulação de uma requisição
        self.firstname = firstname
        self.lastname = lastname
            
    def get_address(self):
        sleep(2)
        return [
            {'rua': 'Rua do desenvolvedor', 'numero':'0'}
        ]
    
    def get_all_user_data(self) -> Dict:
        return {
            'cpf':'111.111.111 - 11',
            'rg ':'7777777'
        }
        
class UserProxy(IUser):
    def __init__(self, firstname:str, lastname:str):
        self.firstname = firstname
        self.lastname = lastname
        
        self._real_user: RealUser
        self._cached_addresses: List[Dict]
        self._all_user_data: Dict
        
    def get_real_user(self):
        if not hasattr(self, '_real_user'):
            self._real_user = RealUser(self.firstname, self.lastname)
    
    def get_address(self):
        self.get_real_user()
        
        if not hasattr(self, '_cached_addresses'):
            self._cached_addresses = self._real_user.get_address()
        
        return self._cached_addresses
            
    def get_all_user_data(self) -> Dict:
        self.get_real_user()
        
        if not hasattr(self, '_cached_addresses'):
            self._all_user_data = self._real_user.get_all_user_data()
        
        return self._all_user_data
    
if __name__ == "__main__":
    jose = UserProxy('Jose', 'Junior ')
    print(jose.firstname)
    print(jose.lastname)
        
    print(jose.get_all_user_data())
    print(jose.get_address())
    
    #Respndendo instantaneamente devido ao proxy
    for x in range(50):
        print(jose.get_address())    
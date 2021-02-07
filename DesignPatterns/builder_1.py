"""
Builder é um padrão de criação que tem a intenção de separar a construção de um objeto complexo
da sua representação, de modo que o mesmo processo de construção possa criar diferentes representações.

Builder te dá a possibilidade de criar objetos passo-a-passo e isso já é possível em python sem este padrão.
"""

from abc import ABC, abstractmethod

class User:
    def __init__(self):
        # O builder não é tão necessário em python pois poderia atribuir o None nos parâmetros do __init__.
        self.firstname = None

class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self):pass

    @abstractmethod
    def add_firstname(self, firstname): pass

    #Para utilizar o builder adicione mais métodos aqui.


class UserBuilder(IUserBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._result = User()

    @property
    def result(self):
        return_data = self._result
        self.reset()
        return return_data

    def add_firstname(self, firstname):
        self._result.firstname = firstname


class UserDirector:
    def __init__(self, builder):
        self.builder = builder

    # Aqui você pode adicionar métodos específicos para serem chamados de acordo com atributos específicos.


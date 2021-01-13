from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor,(int, float)):
            raise ValueError('Saldo precisa ser numérico.')
        self._saldo = valor 

    def depositar(self, valor):
        if not isinstance(valor,(int, float)):
            raise ValueError('Depósito precisa ser numérico.')
        self._saldo += valor

    @abstractmethod
    def sacar(self, valor):
        pass

    def detalhes(self):
        print(f'Agência {self._agencia}', end= ' ')
        print(f'Conta {self._conta}', end= ' ')
        print(f'Saldo {self._saldo}', end= ' ')

class Poupanca(Conta):
    def sacar(self, valor):
        if self._saldo < valor:
            print("Saldo insuficiente.")
            return
        self.saldo -= valor

class Corrente(Conta):
    def __init__(self, agencia, conta, saldo, limite = 100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    def sacar(self, valor):
        if self._saldo + self._limite < valor:
            print("Saldo insuficiente.")
            return
        self.saldo -= valor

    @property
    def limite(self):
        return self._limite





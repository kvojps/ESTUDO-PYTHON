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

    @abstractmethod
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        if not isinstance(valor,(int, float)):
            raise ValueError('O valor deve ser numérico')
        self._saldo += valor
        self.detalhes()
        print('#'*30)

    def detalhes(self):
        print(f'Conta: {self._conta}')
        print(f'Agência: {self._agencia}')
        print(f'Saldo: {self._saldo}')


class Poupanca(Conta):
    def sacar(self, valor):
        if self._saldo < valor:
            print('Saldo insuficiente')
            return
        self._saldo -= valor
        self.detalhes()
        print('#'*30)

class Corrente(Conta):
    def __init__(self, agencia, conta, saldo, limite = 100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    def sacar(self, valor):
        if (self._saldo + self._limite) < valor:
            print('Saldo insuficiente')
        self._saldo -= valor
        self.detalhes()
        print('#'*30)

    def limite(self):
        return self._limite
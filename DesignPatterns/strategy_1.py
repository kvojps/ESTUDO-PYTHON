"""
Strategy é um padrão de projeto comportamental que tem a intenção de definir uma família de algoritmos ,
encapsular cada uma delas e torná-las intercambiáveis.
"""
from __future__ import annotations
from abc import ABC, abstractmethod

class Pedido:
    def __init__(self, total: float, desconto:EstrategiaDesconto):
        self._total = total
        self._desconto = desconto

    @property
    def total(self):
        return self._total

    @property
    def total_com_desconto(self):
        pass
        return self._desconto.calcular(self._total)

class EstrategiaDesconto(ABC):
    @abstractmethod
    def calcular(self, valor:float) -> float:
        pass

class VintePorCento(EstrategiaDesconto):
    def calcular(self, valor:float) -> float:
        return valor - (valor * 0.2)

class CinquentaPorCento(EstrategiaDesconto):
    def calcular(self, valor:float) -> float:
        return valor - (valor * 0.5)

class SemDesconto(EstrategiaDesconto):
    def calcular(self, valor:float) -> float:
        return valor

class AjustarDesconto(EstrategiaDesconto):
    def __init__(self, desconto):
        self._desconto = desconto/100
    
    def calcular(self, valor:float) -> float:
        return valor - (valor * self._desconto)

if __name__ == "__main__":
    desconto_vinte = VintePorCento()
    desconto_cinquenta = CinquentaPorCento()
    sem_desconto = SemDesconto()
    desconto_dez = AjustarDesconto(10)

    pedido = Pedido(1000, desconto_vinte)
    print(pedido.total, pedido.total_com_desconto)

    pedido = Pedido(1000, desconto_cinquenta)
    print(pedido.total, pedido.total_com_desconto)

    pedido = Pedido(1000, sem_desconto)
    print(pedido.total, pedido.total_com_desconto)

    pedido = Pedido(1000, desconto_dez)
    print(pedido.total, pedido.total_com_desconto)
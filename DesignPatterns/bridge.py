"""
Bridge é um padrão de projeto estrutural que tem a intenção de desacoplar 
uma abstração da sua implementação , de modo que as duas possam variar e evoluir independentemente.

-> Adapter é um padrão de projeto estrutural que tem a intenção de permitir que duas classes que seriam 
incompatíveis trabalhem em conjunto através de um adaptador. 

Diferença entre Adapter e bridge(GOF pag.208) - A diferença chave entre esses padrões está nas suas intenções. 
O padrão adapter faz as coisas funcionarem após elas terem sido projetadas , já o bridge faz elas funcionarem 
antes que existam.  
"""

from __future__ import annotations
from abc import ABC, abstractmethod

class IRemoteControl(ABC):
    @abstractmethod
    def increase_volume(self) ->None: pass

    @abstractmethod
    def decrease_volume(self) ->None: pass

    @abstractmethod
    def power(self) ->None: pass
    
class RemoteControl(IRemoteControl):
    def __init__(self, device:IDevice):
        self._device = device

    def increase_volume(self) ->None:
        self._device.volume += 10

    def decrease_volume(self) ->None:
        self._device.volume -= 10
    
    def power(self) ->None:
        self._device.power = not self._device.power
    
class IDevice(ABC):
    @property
    @abstractmethod
    def volume(self) -> int:pass

    @volume.setter
    def volume(self, volume: int) -> None:
        pass

    @property
    @abstractmethod
    def power(self) -> bool:pass
    
    @power.setter
    def power(self, power: bool) -> None:
        pass
    
class TV(IDevice):
    def __init__(self):
        self._volume = 10
        self._power = False
        self._name = self.__class__.__name__
        
    @property
    def volume(self) -> int:
        return self._volume

    @volume.setter
    def volume(self, volume: int) -> None:
        if not self._power:
            print(f'{self._name} está desligada !')
            return
        if volume > 100 or volume < 0:
            return
        
        self._volume = volume
        print(f'Volume atual: {self._volume}')
            
    @property
    def power(self) -> bool:
        return self._power

    @power.setter
    def power(self, power: bool) -> None:
        if power == self._power:
            return
        self._power = power
        power_status = 'ligado' if self._power else 'desligado'
        print(f'Estado da TV: {power_status}')

    
if __name__ == "__main__":
    tv = TV()   
    controle = RemoteControl(tv)
    
    controle.power()
    controle.increase_volume()
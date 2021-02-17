"""
Façade(fachada) é um padrão de projeto estrutural que tem a intenção de fornecer uma interface unificada
para um conjunto de interfaces em um subsistema.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict


class IObservable(ABC):
    """ Observable """

    @property
    @abstractmethod
    def state(self): pass

    @abstractmethod
    def add_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def notify_observers(self) -> None: pass


class WeatherStation(IObservable):
    """ Observable """

    def __init__(self) -> None:
        self._observers: List[IObserver] = []
        self._state: Dict = {}

    @property
    def state(self) -> Dict:
        return self._state

    @state.setter
    def state(self, state_update: Dict) -> None:
        new_state: Dict = {**self._state, **state_update}

        if new_state != self._state:
            self._state = new_state
            self.notify_observers()

    def reset_state(self) -> None:
        self._state = {}
        self.notify_observers()

    def add_observer(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        if observer not in self._observers:
            return

        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()
        print()


class IObserver(ABC):
    @abstractmethod
    def update(self) -> None: pass


class Smartphone(IObserver):
    def __init__(self, name, observable: IObservable) -> None:
        self.name = name
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(f'{self.name} o objeto {observable_name} '
              f'acabou de ser atualizado => {self.observable.state}')
        
class WeatherStationFacade:
    def __init__(self):
        self.estacao_climatica = WeatherStation()

        self.celular = Smartphone('Motorola', self.estacao_climatica)
        self.celular_2 = Smartphone('Motorola', self.estacao_climatica)

        self.estacao_climatica.add_observer(self.celular)
        self.estacao_climatica.add_observer(self.celular_2)
        
    def add_observer(self, observer:IObserver) :
        self.estacao_climatica.add_observer(observer)
    
    def remove_observer(self, observer:IObserver):
        self.estacao_climatica.remove_observer(observer)
        
    def change_state(self, state:Dict):
        self.estacao_climatica.state = state
    
    def reset_state(self):
        self.estacao_climatica.reset_state()
    
    
if __name__ == "__main__":
    estacao_climatica = WeatherStationFacade()
    estacao_climatica.change_state({'temperatura': '45'})
    estacao_climatica.reset_state()
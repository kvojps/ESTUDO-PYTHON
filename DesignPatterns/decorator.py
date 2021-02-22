from __future__ import annotations
from dataclasses import dataclass 
from typing import List
from copy import deepcopy

#INGREDIENTES

@dataclass
class Ingredient:
    price: float

@dataclass
class Bread(Ingredient):
    price: float = 2.00

@dataclass
class Sausage(Ingredient):
    price: float = 5.00

@dataclass
class Bacon(Ingredient):
    price: float = 6.00

@dataclass
class Egg(Ingredient):
    price: float = 2.40

@dataclass
class PotatoSticks(Ingredient):
    price: float = 0.80

@dataclass
class MashedPotatoes(Ingredient):
    price: float = 2.00

@dataclass
class Cheese(Ingredient):
    price: float = 6.00

#HOTDOGS

class Hotdog:
    _name: str
    _ingredients: List[Ingredient]

    @property
    def price(self) -> float:
        return round(sum([
            ingredient.price for ingredient in self._ingredients
        ]),2)

    @property
    def name(self) -> str:
        return self._name 

    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients 

    def __repr__(self):
        return f'{self.name}({self.price}) -> {self.ingredients}'

class SimpleHotdog(Hotdog):
    def __init__(self):
        self._name = 'SimpleHotdog'
        self._ingredients : List[Ingredient] = [
            Bread(),
            Sausage(),
            PotatoSticks()
        ]

class SpecialHotdog(Hotdog):
    def __init__(self):
        self._name = 'SimpleHotdog'
        self._ingredients : List[Ingredient] = [
            Bread(),
            Sausage(),
            PotatoSticks(),
            Bacon(),
            Egg(),
            Cheese(),
            MashedPotatoes()
        ]

#decoradores
class HotdogDecorator(Hotdog):
    def __init__(self, hotdog: Hotdog, ingredient: Ingredient):
        self.hotdog = hotdog
        self._ingredient = ingredient
        self._ingredients = deepcopy(self.hotdog.ingredients)
        self._ingredients.append(self._ingredient)

    @property
    def name(self) -> str:
        return f'{self.hotdog.name} + {self._ingredient.__class__.__name__}'


        
if __name__ == "__main__" :
    simple_hotdog = SimpleHotdog()
    print(simple_hotdog)

    bacon_simple_hotdog = HotdogDecorator(simple_hotdog, Bacon())
    print(bacon_simple_hotdog)

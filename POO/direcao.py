from enum import Enum

class Direcoes(Enum):
    direita = 0
    esquerda = 1
    cima = 2
    baixo = 3

def mover(direcao):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Você não pode mover para essa direção')
    return f'Movendo para {direcao.name}'

print(mover(Direcoes.direita))
print(mover(Direcoes.cima))
print(mover('qualquer lugar'))


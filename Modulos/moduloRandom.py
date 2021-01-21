import random

inteiro = random.randint(10, 20)
flutuante = random.uniform(10,20)

lista = ['jose', 'joao', 'maria', 'joaquim', 'lucas']
sorteio = random.choice(lista)
sorteio_grupo = random.sample(lista, 3)

random.shuffle(lista)


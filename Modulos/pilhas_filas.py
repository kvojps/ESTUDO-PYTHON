"""
Pilha(Stack) - LIFO - last in, first out.
    Exemplo: Pilha de livros que são adicionados um sobre o outro.
Fila(Queue) - FIFO - first in, first out.
    Exemplo: Uma fila de banco(ou qualquer fila da vida real)
Filas podem ter efeitos colaterais em desempenho, porque a cada item alterado, todos
os índices serão modificados.
"""
from collections import deque

# Exemplo de pilha LIFO
livros = list()
livros.append('livro 1')
livros.append('livro 2')
livros.append('livro 3')
livros.append('livro 4')
livros.append('livro 5')
livro_removido = livros.pop()
# print(livros, livro_removido)

#Exemplo de fila FIFO
fila = deque()
fila.append('Jose')
fila.append('Maria')
fila.append('Junior')
fila.append('ferreira')
fila.append('joao')
print(f'Saiu:{fila.popleft()}')
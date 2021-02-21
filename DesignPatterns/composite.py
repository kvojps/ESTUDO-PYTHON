"""
Composite é um padrão de projeto estrutural que permite que você utilize a composição
para criar objetos em estrutura de árvores. O padrão permite aos clientes tratarem de maneira
uniforme objetos individuais (Leaf) e composições de objeto (Composite).

--> Só aplique este padrão em uma estrutura que possa ser representada em formato hierárquico 
    (árvore).

Objetos Composite são objetos mais complexos e com filhos. Geralmente, eles delegam trabalho para os filhos 
usando um método em comum. Objetos Leaf são objetos simples, da ponta e sem filhos. Geralmente, são esses objetos 
que realizam o trabalho real da aplicação.
"""
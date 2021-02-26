def sum(x,y):
    """Soma x e y 
    >>> sum(10,20)
    30
    >>> sum(-10,20)
    10
    >>> sum("-10",20)
    Traceback (most recent call last):
    ...
    AssertionError: X precisa ser um número inteiro ou ponto flutuante
    """
    assert isinstance(x,(int,float)), 'X precisa ser um número inteiro ou ponto flutuante'
    assert isinstance(y,(int,float)), 'y precisa ser um número inteiro ou ponto flutuante'
    return x + y

def subtrai(x,y):
    """Subtrai x e y
    >>> subtrai('10',5) 
    Traceback (most recent call last):
    ...
    AssertionError: X precisa ser um número inteiro ou ponto flutuante
    """
    assert isinstance(x,(int,float)), 'X precisa ser um número inteiro ou ponto flutuante'
    assert isinstance(y,(int,float)), 'y precisa ser um número inteiro ou ponto flutuante'
    return x - y

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
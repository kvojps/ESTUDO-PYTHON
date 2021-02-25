def soma(x,y):
    assert isinstance(x, (float, int)), 'X e Y precisam ser int ou float'
    assert isinstance(y, (float, int)), 'X e Y precisam ser int ou float'
    return x + y

if __name__ == '__main__':
    try:    
        print(soma(5,'10'))
    except AssertionError as erro:
        print(f'Não é possível fazer essa conta: {erro}')
    
    print(soma(5, 10))
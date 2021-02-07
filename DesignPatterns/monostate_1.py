"""
Monostate (ou Borg) - É uma variação do singleton que tem a intenção de garantir que o estado do objeto
seja igual para todas as instâncias. O monostate é melhor para se trabalhar com heranças, isso ao ser relacionado
com o singleton.

"""

class StringReprMixin:
    def __str__(self):
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()

class MonoStateSimple(StringReprMixin):
    _state = {'x': 10,'y': 20}

    def __init__(self, nome=None):
        self.__dict__ = self._state

        if nome is not None:
            self.nome = nome
        
if __name__ == "__main__":
    m1 = MonoStateSimple()
    m2 = MonoStateSimple()
    print(m1)
    print(m2)
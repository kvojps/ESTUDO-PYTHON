class StringReprMixin:
    def __str__(self):
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()

class MonoState(StringReprMixin):
    _state = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state
        return obj

    def __init__(self, nome=None):
        if nome is not None:
            self.nome = nome
        
if __name__ == "__main__":
    m1 = MonoState()
    m2 = MonoState()
    print(m1)
    print(m2)
"""
O singleton tem a intenção de garantir que uma classe tenha somente uma instância
e fornece um ponto global de acesso para a mesma. Muitas desenvolvedores não gostam de utilizar 
o singleton na maioria das vezes.
"""

class AppSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self) -> None:
        """ O init será chamado todas as vezes """
        print('Oi')
        self.tema = 'O tema escuro'
        self.font = '18px'


if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = 'O tema claro'
    print(as1.tema)

    as2 = AppSettings()
    print(as1.tema)
    print(id(as1) == id(as2))
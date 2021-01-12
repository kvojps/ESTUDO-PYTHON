class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado :
            return
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            return
        self._ligado = False
        
"""
Classe voltada para demonstração, o python já 
tem um módulo pra tratar os logs.
"""
class LogMixin:
    @staticmethod
    def write(msg):
        with open('log.log','a+') as f :
            f.write(msg)
            f.write('\n')
    
    def log_info(self, msg):
        self.write(f'INFO : {msg}')
    
    def log_erro(self, msg):
        self.write(f'ERROR : {msg}')

class Smartphone(Eletronico, LogMixin):
    def __init__(self,nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado :
            erro = f'{self._nome} não está ligado'
            print(erro)
            self.log_erro(erro)
            return
      
        if self._conectado :
            erro = f'{self._nome} já está conectado'
            print(erro)
            self.log_erro(erro)
            return

        info = f'{self._nome} está conectado'
        print(info)
        self.log_info(info)
        self._conectado = True
    
    def desconectar(self):
        if not self._conectado:
            erro = 'Seu celular já está desconectado'
            print(erro)
            self.log_erro(erro)
            return

        info = 'Seu celular está desconectado'
        print(info)
        self.log_info(info)
        self._conectado = False


# cell = Smartphone('motorola one')
# cell.conectar()
# cell.desligar()
# cell.ligar()
# cell.conectar()
# cell.conectar()
# cell.conectar()
# cell.desligar()
# cell.conectar()
# cell.desconectar()




"""
Command tem a intenção de encapsular uma solicitação como um objeto, desta forma permitindo parametrizar clientes
com diferentes solicitações, enfileirar ou fazer registro(log) de solicitações e suportar operações que podem ser
desfeitas .

É formado por um cliente(quem orquestra tudo), um invoker(que invoca as solicitações). Um ou vários objetos de 
comando(que fazem a ligação entre o receiver e ação que tem que ser executada) e um receiver(o objeto que vai 
executar a ação no final).

"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict

# receiver(Quem recebe o comando final)
class Light:
    def __init__(self, name:str, room_name:str) -> None:
        self.name = name
        self.room_name = room_name
        self.color = 'Default color'
        
    def on(self) -> None:
        print(F'{self.name} no {self.room_name} está ligada !')
    
    def off(self) -> None:
        print(F'{self.name} no {self.room_name} está desligada !')
        
    def change_color(self, color:str) -> None:
        self.color = color
        print(F'{self.name} no {self.room_name} está ligada na cor {self.color}!')

# Interface de comando
class ICommand(ABC):
    @abstractmethod
    def execute(self) -> None: pass

    @abstractmethod
    def undo(self) -> None: pass

# Comando concreto    
class LightOnCommand(ICommand):
    def __init__(self, light: Light) -> None:
        self.light = light
        
    def execute(self) -> None:
        self.light.on()
        
    def undo(self) -> None:
        self.light.off()

# Comando concreto    
class LightChangeColor(ICommand):
    def __init__(self, light: Light, color:str) -> None:
        self.light = light
        self.color = color
        self._old_color = self.light.color
        
    def execute(self) -> None:
        self._old_color = self.light.color
        self.light.change_color(self.color)
        
    def undo(self) -> None:
        self.light.change_color(self._old_color)
 
# Invoker       
class RemoteController:
    def __init__(self) -> None:
        self._buttons: Dict[str, ICommand] = {}
        
    def add_command(self, name:str, command: ICommand) -> None:
        self._buttons[name] = command
        
    def button_execute(self, name:str) -> None:
        if name in self._buttons:
            self._buttons[name].execute()
    
    def button_undo(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].undo()
            
if __name__ == '__main__':
    luz_quarto = Light('Lâmpada', 'quarto')
    luz_banheiro = Light('Lâmpada', 'banheiro')
    
    quarto_aceso = LightOnCommand(luz_quarto)
    banheiro_aceso = LightOnCommand(luz_banheiro)
    luz_banheiro_azul = LightChangeColor(luz_banheiro,'azul')
    
    controle_remoto = RemoteController()
    controle_remoto.add_command('primeiro botão', quarto_aceso)
    controle_remoto.add_command('segundo botão', luz_banheiro_azul)
    
    controle_remoto.button_execute('primeiro botão')
    controle_remoto.button_execute('segundo botão')
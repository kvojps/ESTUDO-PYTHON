from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('José')
caneta = Caneta('Divers')
maquina = MaquinaDeEscrever()

# Associação entre os objetos: 
escritor.ferramenta = caneta
escritor.ferramenta.escrever()
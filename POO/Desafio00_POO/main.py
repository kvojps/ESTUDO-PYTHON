from banco import Banco
from pessoa import Cliente
from conta import Corrente, Poupanca

banco = Banco()

c0 = Cliente('jose',18)
c1 = Cliente('maria',18)
c2 = Cliente('ferreira',18)

conta0 =  Poupanca(1111, 465124, 0)
conta1 =  Poupanca(2222, 464878, 0)
conta2 =  Poupanca(3333, 154635, 0)

c0.inserir_conta(conta0)
c1.inserir_conta(conta1)
c2.inserir_conta(conta2)

banco.inserir_cliente(c0)
banco.inserir_conta(conta0)

if banco.autenticar(c0):
    c0.conta.depositar(40)
    c0.conta.sacar(20)

else:
    print('Conta não autenticada.')
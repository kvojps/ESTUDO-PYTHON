"""
O padrão de projeto State é um padrão comportamental que tem a intenção de permitir a um objeto mudar seu 
comportamento quando o seu estado interno muda.
O objeto parecerá ter mudado sua classe.
"""
from abc import ABC, abstractmethod


class Order():
    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self):
        self.state.pending()        

    def approve(self):
        self.state.approve()        

    def reject(self):
        self.state.reject()
        
class OrderState(ABC):
    def __init__(self, order:Order):
        self.order = order
        
    @abstractmethod
    def pending(self):pass

    @abstractmethod
    def approve(self):pass

    @abstractmethod
    def reject(self):pass

class PaymentPending(OrderState):
            
    def pending(self):
        print('Pagamento já está como pendente.')

    def approve(self):
        self.order.state = PaymentApproved(self.order)
        print('Pagamento aprovado.')

    def reject(self):
        self.order.state = PaymentRejected(self.order)
        print("Pagamento rejeitado.")

class PaymentApproved(OrderState):

    def pending(self):
        self.order.state = PaymentPending(self.order)
        print("Pagamento pendente.")
        
    def approve(self):
        print("Pagamento já está como aprovado.")

    def reject(self):
        self.order.state = PaymentRejected(self.order)
        print("Pagamento rejeitado.")

class PaymentRejected(OrderState):

    def pending(self):
        print("Pagamento rejeitado não pode ter seu estado alterado pendente.")

    def approve(self):
        print("Pagamento rejeitado não pode ter seu estado alterado para aprovado.")

    def reject(self):
        print("Pagamento já está como rejeitado.")
    
if __name__ == "__main__":
    pedido = Order()
    pedido.pending()
    pedido.approve()
    pedido.reject()
    pedido.approve()
    
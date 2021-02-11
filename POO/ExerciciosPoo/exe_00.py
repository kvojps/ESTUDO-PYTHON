class Bola:
    def __init__(self, cor, material):
        self.cor = cor
        self.material = material
    
    def trocar_cor(self, nova_cor):
        self.cor = nova_cor
        
    def mostra_cor(self):
        print(f'A cor da bola é {self.cor}')
        
if __name__ == "__main__":
    bola = Bola('azul', 'plástico')
    bola.trocar_cor('vermelho')
    bola.mostra_cor()
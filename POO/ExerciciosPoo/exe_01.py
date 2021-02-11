class Quadrado:
    def __init__(self, lado):
        self.lado = lado
        
    def mudar_lado(self, lado):
        self.lado = lado
        
    def calc_area(self):
        print(f'O valor do lado é {self.lado}')
        area = self.lado ** 2
        print(f'Área: {area}')
        
if __name__ == "__main__":
    quadrado = Quadrado(2)
    quadrado.mudar_lado(4)
    quadrado.calc_area()
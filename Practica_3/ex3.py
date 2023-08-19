print('Exercicio 3')
class Circulo:
    pi=3.1416

    def __init__(self, radio):
        self.radio = radio

    # Hallar Area
    def Area(self):
        return self.pi*self.radio**2

c=Circulo(5)
print(c.Area())
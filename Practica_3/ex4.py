print('Exercicio 4')
class Rectangulo:
    def __init__(self, base,altura):
        self.base = base
        self.altura=altura

    # Hallar Area
    def Area(self):
        return self.base*self.altura
#creando rectangulo de base 3 con altura 5
r=Rectangulo(3,5)
print(r.Area())

import math


class Circulo:

    def __init__(self, radio=0):
        self.radio = radio

    def area(self):
        return (self.radio*self.radio)*math.pi

    def perimetro(self):
        return (self.radio * math.pi) * 2

c = Circulo(1)
print(c.area())
print(c.perimetro())

c2 = Circulo()
c2.r = 1
print(c2.area())
print(c2.perimetro())

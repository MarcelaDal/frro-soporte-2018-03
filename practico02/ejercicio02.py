
import math


class Circulo:

    def __init__(self, radio=0):
        self.radio = radio

    def area(self):
        return (self.radio*self.radio)*math.pi

    def perimetro(self):
        return (self.radio * math.pi) * 2


assert Circulo(1).area() == math.pi
assert Circulo(1).perimetro() == 2 * math.pi


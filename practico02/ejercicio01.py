
class Rectangulo:

    def __init__(self, b=0, h=0):
        self.b = b
        self.h = h

    def area(self):
        return self.b * self.h


assert Rectangulo(5, 4).area() == 20
assert Rectangulo(5, 4).area() != 21



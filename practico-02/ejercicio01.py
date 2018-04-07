
class Rectangulo:

    def __init__(self, b=0, h=0):
        self.b = b
        self.h = h

    def area(self):
        return self.b * self.h


r = Rectangulo(1, 2)
print(r.area())

r2 = Rectangulo()
r2.b = 1
r2.h = 2
print(r2.area())

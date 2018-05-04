
from datetime import date
from math import floor
class Persona():

    def __init__(self,fecha_naciemiento):
        self.fecha_nacimiento=fecha_naciemiento

    def edad(self):
        return floor((date.today()-self.fecha_nacimiento).days/365)

assert Persona(date(1996,10,31)).edad()==21
assert Persona(date(1996,10,31)).edad()!=22

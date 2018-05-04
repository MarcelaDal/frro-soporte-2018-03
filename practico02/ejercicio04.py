from practico02.ejercicio06 import Persona
from datetime import date
from math import floor
"""En el enunciado dice año, lo cambie por fecha por inexactitud.
    Ademas use la clase Persona del ejercicio 6
"""
class Estudiante(Persona):
    def __init__(self, fecha_nacimiento, nombre_carrera, fecha_ingreso,
                 total_materias_carrera, cantidad_materias_aprobada):
        super().__init__(fecha_nacimiento)
        self.nombre_carrera=nombre_carrera
        self.fecha_ingreso=fecha_ingreso
        self.total_materias_carrera=total_materias_carrera
        self.cantidad_materias_aprobada=cantidad_materias_aprobada
    def avance(self):
        return (self.cantidad_materias_aprobada*100)/self.total_materias_carrera
    def edad_ingreso(self):
        return floor((self.fecha_ingreso-self.fecha_nacimiento).days/365)

assert Estudiante(date(1996,10,31),"ISI",date(2015,3,3),40,18).edad_ingreso() == 18
assert Estudiante(date(1996,10,31),"ISI",date(2015,3,3),40,18).edad_ingreso() != 19
assert Estudiante(date(1996,10,31),"ISI",date(2015,3,3),40,18).avance() == 45.0
assert Estudiante(date(1996,10,31),"ISI",date(2015,3,3),40,18).avance() != 46.0





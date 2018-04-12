from random import randint


class Persona:

    def __init__(self, nombre='', edad=0, sexo='', peso=0, altura=0):
        self.generar_dni()
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def es_mayor_edad(self):
        if self.edad >= 21:
            return True
        else:
            return False

    def print_data(self):
        print('nombre: '+self.nombre)
        print('sexo: '+str(self.sexo))
        print('dni: '+str(self.dni))
        print('edad: '+str(self.edad))
        print('peso: '+str(self.peso))
        print('altura: '+str(self.altura))

    def generar_dni(self):
        self.dni = randint(00000000, 99999999)


assert Persona('marcela', sexo='f', edad=22, altura=1.75).print_data()
assert Persona('marcela', sexo='f', edad=22, altura=1.75).es_mayor_edad()==True
assert Persona('marcela', sexo='f', edad=22, altura=1.75).es_mayor_edad() != FalseS



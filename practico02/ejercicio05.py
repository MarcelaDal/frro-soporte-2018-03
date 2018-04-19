from practico02.ejercicio04 import Estudiante
from datetime import date

def getDiccionario(estudiantes):
    diccionario={}
    for e in estudiantes:
        if(e.nombre_carrera in diccionario):
            diccionario[e.nombre_carrera]+=1
        else:
            diccionario[e.nombre_carrera]=1
    return diccionario

assert getDiccionario([Estudiante(date(1996,10,31),"ISI",date(2015,3,3),40,18),
                       Estudiante(date(1996,10,31),"IQ",date(2015,3,3),40,18)]) == \
       {'IQ': 1, 'ISI': 1}

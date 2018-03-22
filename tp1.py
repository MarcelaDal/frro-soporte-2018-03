
def max(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


def max_de_tres(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1
    else:
        if n2 > n1 and n2 > n3:
            return n2
        else:
            return n3

def calcula_log(cadena):
    long = len(cadena)
    return long


def is_vowel(letter):
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        return True
    else:
        return False;




def multipl(list):
    result = 1
    for x in list:
        result = result * x
    return result



def inversa(cadena):
    length = len(cadena)
    cadenaInvertida = ""
    for i in range(length):
        cadenaInvertida += cadena[-(i+1)]
    return cadenaInvertida


def es_palindromo(cadena):
    palabraInversa = inversa(cadena)
    i=0
    for p in palabraInversa:
        if p == cadena[i]:
            response = True
            i+= 1
        else:
            response= False
            i+= 1
    return response


def superposicion(lista1, lista2):
    response = False
    for l1 in lista1:
        for l2 in lista2:
            if l1 == l2:
                response = True
    return response



def generar_n_caracteres(n, caracter):
        return str(caracter)*n



def mas_larga(palabra1, palabra2):
    len1 = len(palabra1)
    len2 = len(palabra2)
    if len1>len2:
        return palabra1
    else:
        if len2>len1:
            return palabra2
        else:
            return 'Las dos palabras tienen la misma longitud.'


def count_digits(number):
    strNumer = str(number)
    return len(strNumer)



def sumatoria(number):
    count= 0
    n = int(number)
    for i in range(n):
        count += i+1

    return count


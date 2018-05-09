
#8 
def superposicion(lista1, lista2):
    response = False
    for l1 in lista1:
        for l2 in lista2:
            if l1 == l2:
                response = True

    return response


assert superposicion([1,4,9,3], [4,4,7,5]) == True
assert superposicion([1,6,9,3], [4,4,7,5]) == False

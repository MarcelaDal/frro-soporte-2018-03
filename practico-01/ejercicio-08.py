
#8 
def superposicion(lista1, lista2):
    response = False
    for l1 in lista1:
        for l2 in lista2:
            if l1 == l2:
                response = True

    return response

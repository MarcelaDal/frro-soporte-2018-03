def Divide(a, b):
    try:
        z = a/b
    except ZeroDivisionError as e:
        z = e
    except TypeError as e:
        z = e
    return z


assert Divide(6, 2) == 3
assert isinstance(Divide(6, 0), ZeroDivisionError) == True
assert isinstance(Divide("Seis", 3), TypeError) == True


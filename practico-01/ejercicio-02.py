
#2 
def max_de_tres(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1
    else:
        if n2 > n1 and n2 > n3:
            return n2
        else:
            return n3

assert max_de_tres(5,9,1)  == 9
assert max_de_tres(5,9,1)  != 1
assert max_de_tres(5,9,1)  != 5

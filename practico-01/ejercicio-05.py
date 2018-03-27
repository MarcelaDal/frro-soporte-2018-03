
#5  
def multipl(list):
    result = 1
    for x in list:
        result = result * x
    return result

multipl([1,2,3]) == 6
multipl([1,2,3]) != 8

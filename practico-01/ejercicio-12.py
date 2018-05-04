
#12 
def sumatoria(number):
    count= 0
    n = int(number)
    for i in range(n):
        count += i+1

    return count

assert sumatoria(4) == 10
assert sumatoria(3) != 10

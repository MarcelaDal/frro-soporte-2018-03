
#11 
def count_digits(number):
    strNumer = str(number)
    return len(strNumer)


assert count_digits(123) == 3
assert count_digits(1235) != 3

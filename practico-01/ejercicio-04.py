
#4 
vocales = ['a','e','i','o','u']
def isVocal(a):
  if a in vocales:
    return True
  return False


assert isVocal('a')  == True
assert isVocal('g')  == False

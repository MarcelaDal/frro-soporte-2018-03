#13
def isPrimo(n):
  for x in range(2,n):
    if n%x == 0:
      return False
  return True

assert isPrimo(24) == False
assert isPrimo(11) == True
assert isPrimo(15) != True


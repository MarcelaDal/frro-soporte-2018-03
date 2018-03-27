def inversion(s):
  f= len(s)
  a=''
  for x in range(0,f):
    a+=s[f-x-1]
  return a

#7  
def es_palindromo(s):
  if s==inversion(s):
    return True
  return False

assert es_palindromo('hola') == False
assert es_palindromo('neuquen') == True

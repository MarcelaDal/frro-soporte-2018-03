
#6  
def inversion(s):
  f= len(s)
  a=''
  for x in range(0,f):
    a+=s[f-x-1]
  return a

assert inversion('hola') == 'aloh'
assert inversion('hola') != 'hola'

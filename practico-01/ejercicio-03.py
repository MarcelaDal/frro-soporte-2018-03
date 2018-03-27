#3
def longitud(e):
  x=0
  for a in e:
    x+=1
  return x

assert longitud('hola')  == 4
assert longitud('hola')  != 3


#10 
def mas_larga(lista):
  m=lista[0]
  for e in lista[1:len(lista)]:
    if len(e)>len(m):
      m=e
  return m

assert mas_larga(['hola','hola mundo','h']) == 'hola mundo'
assert mas_larga(['hola','hola mundo','h']) != 'hola'


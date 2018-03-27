
#6  
def inversion(s):
  f=longitud(s)
  a=''
  for x in range(0,f):
    a+=s[f-x-1]
  return a

#15
def programa():
  list=[]
  i=input("Ingresar un numero. Para finalizar ingrese la palabra 'fin':")
  while i!="fin":
    list.append(i)
    i=input("Ingresar un numero:")
    
  print("Maximo:"+str(max(list)))
  print("Minimo:"+str(min(list)))
programa()
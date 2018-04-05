#14  
import random 
laberinto1 = [[False,True,False,False],
              [False,True,True,False],
              [False,True,True,False],
              [False,False,True,False]]

def laberinto(maze,x,y,ax,ay):
  print("Estoy en"+ str([x,y]))
  if(x==len(maze)-1 or x==0 or y==len(maze[0])-1 or y==0):
    print("Encontre la salida:"+str([x,y]))
    return [x,y]
  
  movimientosTentativos=[[x-1,y],[x+1,y],[x,y+1],[x,y-1]]
  if [ax,ay] in movimientosTentativos:
    movimientosTentativos.remove([ax,ay])
  
  movimientosPosibles=[]
  for m in movimientosTentativos:
    if(maze[m[0]][m[1]]):
      movimientosPosibles.append(m)
  
  
  if len(movimientosPosibles)==0:
    if(not(x==ax and y==ay)):
      laberinto(laberinto1,ax,ay,x,y)
  else:
    n=movimientosPosibles[random.randint(0,(len(movimientosPosibles)-1))]
    laberinto(laberinto1,n[0],n[1],x,y)

laberinto(laberinto1,1,2,1,2)
    


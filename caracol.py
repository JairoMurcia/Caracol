def mostrar(x):
    for i in x[0]:
       print(i)
    for i in x[1:]:
       print(i[len(x[0])-1])
   
    for i in range(len(x[0]) - 2 ,-1,-1):
        print(x[len(x)-1][i])
   for i in range(len(x[0]) - 2 ,0,-1):
        print(x[i][0])

def suma_fila(fila):
    if fila==[]:
        return 0
    return int(fila[0])+suma_fila(fila[1:])
    
def suma(matriz):
    
    if matriz==[]:
        return 0
    return suma_fila(matriz[0])+suma(matriz[1:])
    

#print(str(suma([x.split() for x in open('matriz.txt').readlines()]))) 

mostrar([x.split() for x in open('matriz.txt').readlines()])


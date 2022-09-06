# Problemas de las 4 babys
#Labelimg 
import numpy as np
def valido(fil,k, queen,p):
    if p==1:
        for i in range(k+1):
            #print(k,queen[i],fil, i)
            if fil == queen[i]: return True
            elif (abs(k-i)==abs(fil-queen[i])): return True
        return False
    else:
        for i in range(k):
                #print(queen[i+1])
                #print(k,queen[i],fil, i)
                if fil == queen[i]: return True
                elif (abs(k-i)==abs(fil-queen[i])): return True
        return False 

def imprimir(queen):
    board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    coordenada = [0,1,2,3]
    for i in range(4):
        board[queen[i]][coordenada[i]]=1
    board = np.array(board)
    print(board)

def reinas(fila, queen) :       
    p=0
    k=1
    fila[1] = 0
    while k>=0:
        #print(queen, "valor k", k)
        while fila[k]<=4 and valido(fila[k],k,queen,p):
            fila[k] = fila[k]+1
            #print(fila[k])
            p=0
        queen[k] = fila[k]
        #print(queen)
        if fila[k]<=3:
            if k == 3:
                imprimir(queen)
                return True
            else:
                k = k+1
                #print('k act:',k)
                fila[k] = 0
        else:
            k=k-1
            p=1
    return False

fila = [0,0,0,0]
queen = [0,0,0,0]

val= reinas(fila, queen)
print(val)


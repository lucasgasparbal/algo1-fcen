from typing import List


def suma_matriz_fila_col(fila:int,col:int)->int:

    suma:int = 0
    
    for i in range(1,fila+1, 1):
        for j in range(1,col+1,1):
            suma += i + j

    

    return suma



print(suma_matriz_fila_col(2,2))
print(suma_matriz_fila_col(3,3))
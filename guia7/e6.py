import e1
import numpy as np

m1 = [
    [1,2,3],
    [3,2,1],
    [4,5,6],
    [5,1,0]
]

m2 = [
    [1,2,3,4],
    [1,5,6,7],
    [3,6,1,1],
    [4,9,6,8]
]

m3 = [[2,3,4,5,7,8,9,0]]

## 1
def es_matriz(s:list[list[int]])->bool:
    
    for i in range(len(s)):
        if (len(s[i]) != len(s[0])):
            return False
    
    if (len(s) != 0):
        return True
    else:
        return False
    

# print(es_matriz([]))
# print(es_matriz([[1,2,3],[1]]))
# print(es_matriz([[1,2,3,4],[4,3,2,1],[3,2,1,4]]))
# print(es_matriz([[1,2,3],[1,2,3],[3,2,1],[3,1]]))
# print(es_matriz([[1,2,3]]))
# print(es_matriz([[1,2],[2,1]]))

## 2

def filas_ordenadas(m:list[list[int]],res:list[bool]):
    res.clear()
    for fila in m:
        res.append(e1.ordenados(fila))


# res:list[bool] = []

# filas_ordenadas(m1,res)
# print(res)
# filas_ordenadas(m2,res)
# print(res)
# filas_ordenadas(m3,res)
# print(res)

## 3

def columna(m:list[list[int]],c:int)->list[int]:
    col: list[int] = []
    for fila in m:
        col.append(fila[c])

    return col

# print(columna(m1,0))
# print(columna(m3,2))
# print(columna(m2,3))

## 4

def columnas_ordenadas(m:list[list[int]])->list[bool]:
    res:list[bool] = []
    for i in range(len(m[0])):
        res.append(e1.ordenados(columna(m,i)))

    return res

# print(columnas_ordenadas(m1))
# print(columnas_ordenadas(m2))
# print(columnas_ordenadas(m3))


## 5

def transponer(m:list[list[int]])->list[list[int]]:

    res:list[list[int]] = []
    for i in range(len(m[0])):
        res.append(columna(m,i))

    return res

# print(transponer(m1))
# print(transponer(m2))
# print(transponer(m3))

## 6

def quien_gana_tateti(m:list[list[str]])->int:
    x_gana:list[str] = ["X","X","X"]
    o_gana:list[str] = ["O","O","O"]
        
    for i in range(len(m[0])):
        col:list[str] = columna_str(m,i)
        if col == x_gana or m[i] == x_gana:
            return 1
        elif col == o_gana or m[i] == o_gana:
            return 0


    for diag in [diagonal(m),diagonal_cruzada(m)]:   
        if diag == x_gana:
            return 1
        elif diag == o_gana:
            return 0
    
    return 2


def columna_str(m:list[list[str]],c:int)->list[str]:
    res:list[str] = []
    for fila in m:
        res.append(fila[c])
    
    return res

def diagonal(m:list[list[str]])->list[str]:
    res:list[str] = []
    for i in range(len(m)):
        res.append(m[i][i])
    
    return res

def diagonal_cruzada(m:list[list[str]])->list[str]:
    res:list[str] = []
    for i in range(len(m)):
        res.append(m[i][len(m)-1-i])
    return res

# tateti1 = [
#     ["X","X","X"],
#     ["O","","O"],
#     ["X","O","X"]
# ]

# tateti2 = [
#     ["X","O",""],
#     ["X","","O"],
#     ["X","O","X"]
# ]

# tateti3 = [
#     ["X","X","O"],
#     ["O","","O"],
#     ["X","O","O"]
# ]

# tateti4 = [
#     ["X","X","O"],
#     ["X","O","X"],
#     ["O","X","O"]
# ]

# tateti5 = [
#     ["X","X","O"],
#     ["X","X","O"],
#     ["O","O","X"]
# ]

# tateti6 = [
#     ["O","X","O"],
#     ["X","O","O"],
#     ["X","O","X"]
# ]

# for tateti in [tateti1,tateti2,tateti3,tateti4,tateti5,tateti6]:
#     print(quien_gana_tateti(tateti))

## 7

def elevar_matriz_random(d:int,p:int)->list[list[int]]:
    m:list[list[int]] = np.random.randint(100,size=(d,d))

    return matriz_potencia(m,p)

# def crear_matriz_random(df:int,dc:int)->list[list[int]]:
#     res:list[list[int]] = []
#     for i in range(df):
#         fila:list[int] = []
#         for j in range(dc):
#             fila.append(np.random.randint(0))
#         res.append(fila)
    
#     return res

def matriz_potencia(m:list[list[int]],p:int)->list[list[int]]:
    res = m

    for h in range(p):
        new_res:list[list[int]] = []
        for i in range(len(m)):
            new_res.append([])
            for j in range(len(m[0])):
                col:list[int] = columna(m,j)
                new_res[i].append(producto_vectorial(m[i],col))
            
        
        res = new_res
    
    return res


def producto_vectorial(v1:list[int],v2:list[int])->int:
    num:int = 0
    for i in range(len(v1)):
        num += v1[i]*v2[i]

    return num

# matriz_2x2 = [[1,3],
#               [3,4]]
# print(elevar_matriz_random(2,2))
# print(matriz_potencia(matriz_2x2,2))
    





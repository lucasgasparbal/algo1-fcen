import e1

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

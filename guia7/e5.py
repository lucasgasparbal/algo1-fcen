
## 1
def pertenece_a_cada_uno_version_1(s:list[list[int]],e:int,res:list[bool]):
    res.clear()
    for i in range(len(s)):
        if e in s[i]:
            res.append(True)
        else:
            res.append(False)
    
    


matriz:list[list[int]] = [
    [1,2,3,4,5],
    [0,1,0,3,0],
    [90,45,13,1],
    [120,3,2,1,0]
]

res:list[bool] = []
# pertenece_a_cada_uno_version_1(matriz,1,res)
# print(res)

# pertenece_a_cada_uno_version_1(matriz,2,res)
# print(res)

# pertenece_a_cada_uno_version_1(matriz,0,res)
# print(res)

# pertenece_a_cada_uno_version_1(matriz,-15,res)
# print(res)

## 2
def pertenece_a_cada_uno_version_2(s:list[list[int]],e:int,res:list[bool]):
    pertenece_a_cada_uno_version_1(s,e,res)

# pertenece_a_cada_uno_version_2(matriz,0,res)
# print(res)

## 3

def pertenece_a_cada_uno_version_3(s:list[list[int]],e:int)->list[bool]:
    res:list[bool] = []
    pertenece_a_cada_uno_version_1(s,e,res)
    return res



# print(pertenece_a_cada_uno_version_3(matriz,1))

## 4
#   El cambio en al especificación del punto 3 con el punto 1 esta definido porque la especificación del punto 3 tiene un parámetro de entrada menos, pero devuelve la lista booleana
# En cambio la especificación del 1 indica que el resultado es un parámetro de entrada de tipo out, con lo cual no importa su estado al iniciar la ejecución de la función
# pero si debe cumplir con el asegura.
#
# Una implementación del punto 2 puede ser implementación del punto 1 pues su segundo asegura es idéntico pero el primer asegura del punto 1 *|res| >= |s|* implica, y por lo tanto
# es mas fuerte que el primer asegura del punto 2 *|res| = |s|*. Pero una implementación del punto 1 puede ser invalida para el punto 2, pues se puede dar que |res| > |s|
# y eso sea solución valida del punto 1, pero no cumple |res| = |s| y por lo tanto no es valida para el punto 2. 
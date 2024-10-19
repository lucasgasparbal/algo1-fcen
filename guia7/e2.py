import e1
## 1

def cerosEnPosicionesPares(s:list[int]):
    for i in range(len(s)):
        if i % 2 == 0:
            s[i] = 0


# s = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# cerosEnPosicionesPares(s)
# print(s)

## 2

def cerosEnPosicionesPares2(s:list[int])->list[int]:
    res:list[int] = []
    for i in range(len(s)):
        if i % 2 == 0:
            res.append(0)
        else:
            res.append(s[i])

    return res

# s = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# print(cerosEnPosicionesPares2(s))
# print(s)

## 3

def sinVocales(s:str)->str:
    res = ""
    for letra in s:
        if not esVocal(letra):
            res += letra
    
    return res

def esVocal(letra:str)->bool:
    vocales:list[str]=["a","e","i","o","u"]

    return letra in vocales

print(sinVocales("alejo"))
print(sinVocales("solo se que no se nada"))
print(sinVocales("lo profundo ama a la mascara"))

## 4

def reemplaza_vocales(s:str)->str:
    res:str = ""
    for i in range(len(s)):
        if( esVocal(s[i])):
            res += "-"
        else:
            res += s[i]

    return res

# print(reemplaza_vocales("alejo"))
# print(reemplaza_vocales("solo se que no se nada"))
# print(reemplaza_vocales("lo profundo ama a la mascara"))


## 5

def da_vuelta_str(s:str)->str:
    res:str = ""
    for i in range(len(s)):
        res += s[len(s)-1-i]
    return res

# print(da_vuelta_str("alejo"))
# print(da_vuelta_str("solo se que no se nada"))
# print(da_vuelta_str("lo profundo ama a la mascara"))

## 6

def eliminar_repetidos(s:str)->str:
    res:str = ""
    letras_repetidas:list[str] = []
    for letra in s:
        if not letra in letras_repetidas:
            res += letra
            letras_repetidas.append(letra)


    return res

print(eliminar_repetidos("aleja"))
print(eliminar_repetidos("alejo"))
print(eliminar_repetidos("solo se que no se nada"))

##punto 1

def pertenece1(s:list[int],e:int)->bool:
    for elem in s:
        if ( elem == e):
            return True
        
    return False

# print(pertenece1([1,2,3],1))
# print(pertenece1([1,2,3],4))
# print(pertenece1([],4))

def pertenece2(s:list[int],e:int)->bool:
    for i in range(0,len(s),1):
        if ( s[i] == e):
            return True
        
    return False

# print(pertenece2([1,2,3],1))
# print(pertenece2([1,2,3],4))
# print(pertenece2([],4))

def pertenece3(s:list[int],e:int)->bool:
    contador:int = 0
    while(contador < len(s)):
         if(s[contador] == e):
             return True
         contador += 1

    return False

# print(pertenece3([1,2,3],1))
# print(pertenece3([1,2,3],4))
# print(pertenece3([],4))



## punto 2


def divide_a_todos(s:list[int],e:int):
    for elem in s:
        if(not elem % e == 0):
            return False
    return True

# print(divide_a_todos([120,24,36,6],6))
# print(divide_a_todos([120,24,36,6,15],6))
# print(divide_a_todos([5,120,24,36,6,15],2))
# print(divide_a_todos([120,24,7,36,6,15],2))
# print(divide_a_todos([2],2))
# print(divide_a_todos([],2))
# print(divide_a_todos([13],1))

## punto 3

def suma_total(s:list[int])->int:
    sum:int = 0
    for elem in s:
        sum += elem
    return sum

# print(suma_total([3,5,10,2]))
# print(suma_total([10,10,10,10]))

## punto 4

def maximo(s:list[int])->int:
    max:int = s[0]

    for elem in s:
        if(elem > max):
            max = elem

    return max

# print(maximo([1]))
# print(maximo([1,2,3,4,5,6]))
# print(maximo([16,5,4,3,2,1]))
# print(maximo([0,-25,65,178,32,12]))

## punto 5

def minimo(s:list[int])->int:
    min:int = s[0]

    for elem in s:
        if(elem < min):
            min = elem

    return min

# print(minimo([1]))
# print(minimo([1,2,3,4,5,6]))
# print(minimo([16,5,4,3,2,1]))
# print(minimo([0,-25,65,178,32,12]))

## punto 6

def ordenados(s:list[int])->bool:
    
    for i in range(len(s)-1):
        if not (s[i]<s[i+1]):
            return False
        
    return True

# print(ordenados([]))
# print(ordenados([1]))
# print(ordenados([1,2,3,4,5]))
# print(ordenados([1,3,2,4,2]))
# print(ordenados([1,2,3,4,4,5]))

## punto 7

def pos_maximo(s:list[int])->bool:

    if len(s) == 0:
        return -1
    
    max:int = maximo(s)

    for i in range(len(s)):
        if max == s[i]:
            return i


# print(pos_maximo([]))
# print(pos_maximo([1]))
# print(pos_maximo([1,2,3,4,5,6]))
# print(pos_maximo([1,2,9,3,4,5]))

## punto 8

def pos_minimo(s:list[int])->bool:

    if len(s) == 0:
        return -1
    
    min:int = minimo(s)

    for i in range(len(s)):
        if min == s[i]:
            return i
        

# print(pos_minimo([]))
# print(pos_minimo([1]))
# print(pos_minimo([1,2,3,-4,5,6]))
# print(pos_minimo([1,2,9,3,4,-5]))

## punto 9

def alguna_palabra_larga(palabras:list[str])->bool:
    for palabra in palabras:
        if len(palabra) > 7:
            return True
    return False

# print(alguna_palabra_larga(["termo", "gato", "tener", "jirafas"]))

# print(alguna_palabra_larga(["termo", "gato", "tener", "jirafas","jirafales"]))

## punto 10

def palindromo(palabra:str)->bool:
    if len == 0 or len == 1:
        return True
    
    for i in range(len(palabra)):
        if not (palabra[i] == palabra[len(palabra)-1-i]):
            return False
        
    return True


# print(palindromo("hola"))

# print(palindromo("aooa"))
# print(palindromo("adoda"))

## punto 11

def tres_numeros_consecutivos(numeros:list[int])->bool:
    if( len(numeros) < 3): 
        return False
    
    for i in range(len(numeros)-2):
        if (numeros[i] == numeros[i+1] and numeros [i] == numeros [i+2]):
            return True
        

# print(tres_numeros_consecutivos([1]))

# print(tres_numeros_consecutivos([1,1]))

# print(tres_numeros_consecutivos([1,1,1]))
# print(tres_numeros_consecutivos([1,2,2,2]))
# print(tres_numeros_consecutivos([1,3,3,2,1,4,4,4,5,6,7]))
# print(tres_numeros_consecutivos([1,3,3,2,1,4,4,5,6,7]))

## punto 12

def tres_vocales_distintas(palabra:str)->bool:
    vocales:list[str]=["a","e","i","o","u"]

    for letra in palabra:
        if letra_pertenece(letra,vocales):
            vocales.remove(letra)
    
    return (len(vocales) < 3)

def letra_pertenece(letra:str,lista:list[str])->bool:
    
    for x in lista:
        if(letra == x):
            return True
    
    return False

# print(tres_vocales_distintas("dfghjkl"))
# print(tres_vocales_distintas("aaa"))
# print(tres_vocales_distintas("a"))
# print(tres_vocales_distintas("aeiou"))
# print(tres_vocales_distintas("alejo"))

## punto 13

def inicio_secuencia_ordenada_mas_larga(lista:list[int])->int:

    secuencia:list[int] = obtener_secuencia_ordenada_mas_larga(lista)

    for i in range(len(lista)):
        j:int = 0
        while (j < len(secuencia) and lista[i+j]==secuencia[j]):
            j += 1
        if (j == len(secuencia)):
            return i
                

def obtener_secuencia_ordenada_mas_larga(lista:list[int])->int:


    secuencias:list[list[int]] = obtener_secuencias_ordenadas(lista)
    secuencia_mas_larga:list[int] = []
    for secuencia in secuencias:
        if(len(secuencia) > len(secuencia_mas_larga)):
            secuencia_mas_larga = secuencia

    return secuencia_mas_larga


def obtener_secuencias_ordenadas(lista:list[int])->int:
    secuencias:list[list[int]] = []

    secuencia_actual:list[int] = []

    for num in lista:
        copia_secuencia_actual:list[int] = secuencia_actual.copy()
        if(len(secuencia_actual) == 0):
            secuencia_actual.append(num)
        elif(num < copia_secuencia_actual.pop()):
            secuencias.append(secuencia_actual)
            secuencia_actual = [num]
        else:   
            secuencia_actual.append(num)

    if(len(secuencia_actual) > 0 ):
        secuencias.append(secuencia_actual)
    return secuencias

# print(inicio_secuencia_ordenada_mas_larga([1]))
# print(inicio_secuencia_ordenada_mas_larga([1,2,1,2,3]))
# print(inicio_secuencia_ordenada_mas_larga([1,2,1,2,1,2,3,1,2,1,2,1,2,3,4,1,2,1,2,1,2,3]))
# print(inicio_secuencia_ordenada_mas_larga([1,2,3,4,5,6,7,8,9,10]))
# print(inicio_secuencia_ordenada_mas_larga([1,3,1,3,1,3,9,17,28,1,1,1,5,7,19,24,17]))
# print(inicio_secuencia_ordenada_mas_larga([1,2,3,1,2,3]))


## punto 14

def cantidad_digitos_impares(s:list[int])->int:

    digitos_impares_de_lista:list[int] = []

    for num in s:
        for impar in digitos_impares(num):
            digitos_impares_de_lista.append(impar)

    return len(digitos_impares_de_lista)


def digitos_impares(num:int)->list[int]:
    digitos:list[int] = []
    while( num > 10):
        digito:int = num % 10
        if(digito % 2 != 0):
            digitos.append(digito)
        
        num = num // 10


    if (num % 2 != 0):
        digitos.append(num)
    
    return digitos

# print(cantidad_digitos_impares([1]))
# print(cantidad_digitos_impares([2]))
# print(cantidad_digitos_impares([1,2,3]))
# print(cantidad_digitos_impares([54,53,21,19,35,47,4895]))
# print(cantidad_digitos_impares([57, 2383, 812, 246]))

    



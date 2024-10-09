
def alguno_es_0(n:int,m:int)->bool:
    return (n == 0 or m == 0)

# print(alguno_es_0(0,1))
# print(alguno_es_0(12,0))
# print(alguno_es_0(11,1312))

def ambos_son_0(n:int,m:int)->bool:
    return(n== 0 and m == 0)

# print(ambos_son_0(0,0))
# print(ambos_son_0(1,0))
# print(ambos_son_0(1,1))
# print(ambos_son_0(0,1))

def es_nombre_largo(nombre:str)->bool:

    longitud_nombre:int = len(nombre)

    return (3<= longitud_nombre and longitud_nombre <= 8 )


# print(es_nombre_largo("ola"))
# print(es_nombre_largo("abcdabcd"))
# print(es_nombre_largo("abcdab"))
# print(es_nombre_largo("abcabcabcabc"))
# print(es_nombre_largo("ab"))

def es_bisiesto(anio:int)->bool:

    return (anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0))

print(es_bisiesto(2020))
print(es_bisiesto(2024))
print(es_bisiesto(2019))
print(es_bisiesto(2300))

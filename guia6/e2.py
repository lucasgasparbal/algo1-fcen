import math

def imprimir_saludo(nombre:str):
    print("Hola "+nombre)

def raiz_cuadrada_de(numero:float)->float:
    return math.sqrt(numero)


def fahrenheit_a_celsius(temp_far:float)->float:
    return ((temp_far-32)*5/9)

def imprimir_dos_veces(estribillo:str):
    print(estribillo*2)

def es_multiplo_de(n:int,m:int)->bool:
    return (n % m == 0)

def es_par(n:int)->bool:
    return es_multiplo_de(n,2)

def cantidad_de_pizzas(comensales:int,min_cant_porciones:int)->int:
    cant_porciones_total:int = comensales*min_cant_porciones

    if (cant_porciones_total % 8 == 0):
        return (cant_porciones_total/8)


    cant_pizzas:int = ((cant_porciones_total - (cant_porciones_total % 8))/8)+1

    return cant_pizzas



    

#imprimir_saludo("Jorge")


# print(raiz_cuadrada_de(9))

# print(raiz_cuadrada_de(15))

# print(fahrenheit_a_celsius(100))

# print(fahrenheit_a_celsius(95))


# imprimir_dos_veces("esto es una cancion")

# print(es_multiplo_de(108404,2))

# print(es_multiplo_de(153,4))

# print(es_par(5))

# print(es_par(10702))

print(cantidad_de_pizzas(1,3))

print(cantidad_de_pizzas(2,4))

print(cantidad_de_pizzas(6,3))

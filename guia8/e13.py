from queue import Queue as Cola
import random

## 1

def armar_secuencia_de_bingo()->Cola[int]:
    numeros:list[int] = []
    posiciones:list[int] = []
    for i in range(100):
        posiciones.append(i)    
    
    for i in range(100):
        posicion:int = random.choice(posiciones)
        posiciones.remove(posicion)
        numeros.insert(i,posicion)
    bolillero:Cola[int] = Cola()
    for elem in numeros:
        bolillero.put(elem)
    
    return bolillero

def printCola(cola:Cola):
    aux:Cola = Cola()
    lista:list = []
    while not cola.empty():
        elem = cola.get()
        aux.put(elem)
        lista.append(elem)

    while not aux.empty():
        cola.put(aux.get())
    print(lista)
    print(len(lista))

def bolilleroValido(bolillero:Cola[int])->bool:
    lista:list[int] = cola_a_lista(bolillero)

    for i in range(99):
        if not pertenece(i,lista):
            return False

    return True

def cola_a_lista(cola:Cola)->list:
    aux:Cola = Cola()
    lista:list = []
    while not cola.empty():
        elem = cola.get()
        lista.append(elem)
        aux.put(elem)
    while not aux.empty():
        cola.put(aux.get())

    return lista

## 2
def jugar_carton_de_bingo( carton:list[int], bolillero:Cola[int])->int:
    bolillero_aux:Cola[int] = Cola()

    cantidad_turnos:int = 0
    while not bolillero.empty():
        bola_actual:int = bolillero.get()
        bolillero_aux.put(bola_actual)
        if len(carton) > 0:
            cantidad_turnos += 1
        
        if pertenece(bola_actual,carton):
            carton.remove(bola_actual)
    
    while not bolillero_aux.empty():
        bolillero.put(bolillero_aux.get())

    return cantidad_turnos


def pertenece(n:int,l:list[int])->bool:
    for elem in l:
        if elem == n:
            return True

    return False

bolillero = armar_secuencia_de_bingo()

# printCola(bolillero)
# print(bolilleroValido(bolillero))

# print(jugar_carton_de_bingo([1,66,43,22,14,16],bolillero))
# printCola(bolillero)

from queue import Queue as Cola
import random

def generar_nros_al_azar(cantidad:int,desde:int,hasta:int)->Cola[int]:
    res:Cola[int] = Cola()
    for i in range(cantidad):
        res.put(random.randint(desde,hasta))
    
    return res

def printCola(c:Cola):
    aux:Cola = Cola()
    lista:list = []
    while not c.empty():
        elem = c.get()
        aux.put(elem)
        lista.append(elem)

    print(lista)

    while not aux.empty():
        c.put(aux.get())    


# cola = generar_nros_al_azar(15,-25,25)
# printCola(cola)    
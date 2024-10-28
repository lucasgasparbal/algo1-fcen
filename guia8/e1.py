from queue import LifoQueue as Pila
import  random

def generar_nros_al_azar(cantidad:int,desde:int,hasta:int)->Pila[int]:
    res:Pila[int] = Pila()
    for i in range(cantidad):
        res.put(random.randint(desde,hasta))
    
    return res


def printPila(pila:Pila)->None:
    aux:list = []
    while not pila.empty():
        elem = pila.get()
        aux.append(elem)

    aux.reverse()

    print(aux)

    while (len(aux) > 0) :
        pila.put(aux.pop(0))

#printPila(generar_nros_al_azar(6,-170,1259))
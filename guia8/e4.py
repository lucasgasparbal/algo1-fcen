from queue import LifoQueue as Pila
import e1
import e2

def buscar_nota_maxima(p:Pila[tuple[str,int]])->tuple[str,int]:
    copia:Pila[tuple[str,int]] = e2.copiarPila(p)

    maximoActual:tuple[str,int] = copia.get()
    
    while not copia.empty():
        actual:tuple[str,int] = copia.get()
        if maximoActual[1] < actual[1]:
            maximoActual = actual

    return maximoActual

# pila1 = Pila()

# pila1.put(("a",10))

# pila2 = Pila()
# for elem in [("a",4),("b",0),("c",7),("z",5),("k",10)]:
#     pila2.put(elem)

# for pila in [pila1,pila2]:
#     e1.printPila(pila)
#     print(buscar_nota_maxima(pila))
#     e1.printPila(pila)
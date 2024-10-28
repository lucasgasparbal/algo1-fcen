from queue import LifoQueue as Pila
import e1

def cantidad_elementos(p:Pila[int])->int:
    aux:Pila[int] = copiarPila(p)
    cant:int = 0
    while not aux.empty():
        aux.get()
        cant += 1

    return cant

def copiarPila(pila:Pila)->Pila:
    res:Pila = Pila()
    aux:Pila = Pila()
    while not pila.empty():
        aux.put(pila.get())
    while not aux.empty():
        elem = aux.get()
        pila.put(elem)
        res.put(elem)

    return res



# pila1 = e1.generar_nros_al_azar(10,0,9)
# pila2 = e1.generar_nros_al_azar(0,0,0)
# pila3 = e1.generar_nros_al_azar(7,0,152)

# for pila in [pila1,pila2,pila3]:
#      e1.printPila(pila)
#      print(cantidad_elementos(pila))
#      e1.printPila(pila)

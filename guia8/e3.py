from queue import LifoQueue as Pila
import e1
import e2

def buscar_el_maximo(p:Pila[int])->int:
    copia:Pila[int] = e2.copiarPila(p)

    maximo_actual:int = copia.get()
    while not copia.empty():
        elem:int = copia.get()
        if (elem > maximo_actual):
            maximo_actual = elem
    
    return maximo_actual


# pila1 = e1.generar_nros_al_azar(1,0,10)
# pila2 = e1.generar_nros_al_azar(6,-156,1867)

# for pila in [pila1,pila2]:
#     e1.printPila(pila)
#     print(buscar_el_maximo(pila))
#     e1.printPila(pila)

from queue import Queue as Cola
import e8
def buscar_el_maximo(c:Cola[int])->int:

    aux:Cola = Cola()

    max:int = c.get()
    aux.put(max)
    while not c.empty():
        elem:int = c.get()
        aux.put(elem)
        if elem > max:
            max = elem
    
    while not aux.empty():
        c.put(aux.get())

    return max


# c1 = e8.generar_nros_al_azar(1,0,5)
# c2 = e8.generar_nros_al_azar(8,0,9)


# for c in [c1,c2]:
#     e8.printCola(c)
#     print(buscar_el_maximo(c))
#     e8.printCola(c)




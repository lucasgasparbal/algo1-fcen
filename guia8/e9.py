from queue import Queue as Cola
import e8

def cantidad_elementos(c:Cola)->int:
    cant:int = 0
    aux:Cola = Cola()
    while not c.empty():
        aux.put(c.get())
        cant += 1
    
    while not aux.empty():
        c.put(aux.get())

    return cant


#c = e8.generar_nros_al_azar(15,0,9)
# e8.printCola(c)
# print(cantidad_elementos(c))
# e8.printCola(c)

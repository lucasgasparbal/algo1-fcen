from queue import Queue as Cola
import e8

def intercalar(c1:Cola,c2:Cola):

    aux1:Cola = Cola()
    aux2:Cola = Cola()
    res:Cola = Cola()
    turno:int = 1
    while not c2.empty():
        if turno % 2 == 0:
            elem = c2.get()
            aux2.put(elem)
        else:
            elem = c1.get()
            aux1.put(elem)
        
        res.put(elem)
        turno += 1
    
    while not aux1.empty():
        c2.put(aux2.get())
        c1.put(aux1.get())

    return res


c1 = e8.generar_nros_al_azar(4,0,4)
c2 = e8.generar_nros_al_azar(4,5,9)

for c in [c1,c2]:
    e8.printCola(c)

e8.printCola(intercalar(c1,c2))

for c in [c1,c2]:
    e8.printCola(c)

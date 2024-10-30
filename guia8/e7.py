from queue import LifoQueue as Pila
import e1
import e2

def intercalar(p1:Pila,p2:Pila)->Pila:
    copia_p1:Pila = e2.copiarPila(p1)
    copia_p2:Pila = e2.copiarPila(p2)

    alreves:Pila = Pila()

    turno:int = 1
    while not copia_p2.empty():
        if turno % 2 == 0:
            alreves.put(copia_p2.get())
        else:
            alreves.put(copia_p1.get())
        turno += 1

    res:Pila = Pila()
    while not alreves.empty():
        res.put(alreves.get())

    return res

p1 = e1.generar_nros_al_azar(9,0,10)
e1.printPila(p1)
p2 = e1.generar_nros_al_azar(9,11,20)
e1.printPila(p2)

e1.printPila(intercalar(p1,p2))

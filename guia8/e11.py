from queue import Queue as Cola
import e8

def buscar_nota_minima(notas:Cola[tuple[str,int]])->tuple[str,int]:
    aux:Cola[tuple[str,int]] = Cola()

    minimo:tuple[str,int] = notas.get()
    aux.put(minimo)
    while not notas.empty():
        elem:tuple[str,int] = notas.get()
        aux.put(elem)
        if elem[1] < minimo[1]:
            minimo = elem
        
    while not aux.empty():
        notas.put(aux.get())
    
    return minimo


notas1 = Cola()
notas1.put(["a",10])

notas2 = Cola()

for elem in [["a",10],["b",7],["c",1],["d",8],["e",4]]:
    notas2.put(elem)


for c in [notas1,notas2]:
    e8.printCola(c)
    print(buscar_nota_minima(c))
    e8.printCola(c)
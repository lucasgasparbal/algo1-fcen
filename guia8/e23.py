from queue import LifoQueue as Pila


def invertir_lineas(nombre_archivo:str):
    archivo:TextIO  = open(nombre_archivo,"r",encoding="utf-8")
    invertido:TextIO  = open(nombre_archivo + "_reverso.txt","w",encoding="utf-8")
    pila_lineas:Pila = Pila()
    for line in archivo.readlines():
        pila_lineas.put(line)

    texto:str = pila_lineas.get()+"\n"

    while not pila_lineas.empty():
        texto += pila_lineas.get()

    invertido.write(texto)

    archivo.close()
    invertido.close()

# invertir_lineas("e18.txt")
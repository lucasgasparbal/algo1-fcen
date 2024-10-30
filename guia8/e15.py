#
# problema atencion_a_clientes(in c:Cola[[char] x Z x Bool x Bool]): Cola[[char] x Z x Bool x Bool] {
#
#   req: True
#
#   asegura: res es una cola con los elementos de c tal que cumplen el siguiente orden:
#               sean x, y elementos de c: 
#               x < y <-> x3 = True ^ y3 = False || x2 = True ^ y2 = False ||  x < y en c
#               
#}
#

from queue import Queue as Cola
import e8

def atencion_a_clientes(clientes:Cola[tuple[str,int,bool,bool]])->Cola[tuple[str,int,bool,bool]]:

    aux:Cola[tuple[str,int,bool,bool]] = Cola()
    res:Cola[tuple[str,int,bool,bool]] = Cola()
    prioritarios:Cola[tuple[str,int,bool,bool]] = Cola()
    preferenciales:Cola[tuple[str,int,bool,bool]] = Cola()
    otros:Cola[tuple[str,int,bool,bool]] = Cola()

    while not clientes.empty():
        elem = clientes.get()
        aux.put(elem)
        if elem[3]:
            prioritarios.put(elem)
        elif elem[2]:
            preferenciales.put(elem)
        else:
            otros.put(elem)

    for cola in [prioritarios,preferenciales,otros]:
        while not cola.empty():
            res.put(cola.get())
    
    while not aux.empty():
        clientes.put(aux.get())
    
    return res


# l1 = [["a",1,False,False],["b",2,False,False],["C",3,False,False]]

# l2 = [["a",1,False,True],["b",2,False,False],["C",3,False,False],["D",3,False,True],["E",3,True,False],["X",4,True,True],["Y",5,False,False],["W",6,True,False],["Q",7,True,False]]

# c1 = Cola()
# c2 = Cola()
# for elem in l1:
#     c1.put(elem)

# for elem in l2:
#     c2.put(elem)

# for c in [c1,c2]:
#     e8.printCola(c)
#     e8.printCola(atencion_a_clientes(c))
#     e8.printCola(c)
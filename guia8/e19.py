
from queue import LifoQueue as Pila
import e16
import e1
historiales:dict[str,Pila[str]] = {}

def visitar_sitio(historiales:dict[str,Pila[str]], usuario:str,sitio:str):
    if not e16.pertenece(historiales.keys(),usuario):
        historiales[usuario] = Pila()

    historiales[usuario].put(sitio)


def navegar_atras(historiales:dict[str,Pila[str]], usuario:str):
    primero:str = historiales[usuario].get()
    segundo:str = historiales[usuario].get()

    for pagina in [segundo,primero,segundo]:
        historiales[usuario].put(pagina)



# historiales = {}
# visitar_sitio(historiales, "Usuario1", "google.com")
# print("Usuario1 visita google.com")
# e1.printPila(historiales["Usuario1"])
# visitar_sitio(historiales, "Usuario1", "facebook.com")
# print("Usuario1 visita facebook.com")
# e1.printPila(historiales["Usuario1"])
# print("Usuario1 navega hacia atras")
# navegar_atras(historiales, "Usuario1")
# e1.printPila(historiales["Usuario1"])
# visitar_sitio(historiales, "Usuario2", "youtube.com")
# print("Usuario2 navega a youtube.com")
# e1.printPila(historiales["Usuario2"])

    

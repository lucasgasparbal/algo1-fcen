from queue import LifoQueue as Pila
import e1
import e2


def esta_bien_balanceada(s:str)->bool:
    pila_evaluacion:Pila = Pila()
    for char in s:
        if char == "(":
            pila_evaluacion.put("(")
        elif char ==")":
            if pila_evaluacion.empty():
                return False
            else:
                pila_evaluacion.get()
            
    return pila_evaluacion.empty()

# print(esta_bien_balanceada("1 + 2"))
# print(esta_bien_balanceada("(3 + 2*5)"))
# print(esta_bien_balanceada("(12-5"))
# print(esta_bien_balanceada("1 + ) 2 x 3 ( ( )"))
# print(esta_bien_balanceada("10 ∗ ( 1 + ( 2 ∗ ( −1)))"))
# print(esta_bien_balanceada("1 + ( 2 x 3 − ( 2 0 / 5 ) )"))

from queue import Queue as Cola
import e8

def n_pacientes_urgentes(c:Cola[tuple[int,str,str]])->int:
    aux:Cola[tuple[int,str,str]] = Cola()

    cant: int = 0
    
    while not c.empty():
        paciente:tuple[int,str,str] = c.get()
        aux.put(paciente)
        if 1 <= paciente[0] and paciente[0] <= 3:
            cant += 1

    while not aux.empty():
        c.put(aux.get())

    return cant


pacientes1 = Cola()

for elem in [[10,"laura","otorrinolaringología"],[1,"jorge","cardiopatía"],[9,"Juan","Traumatología"],[2,"Elena","Bromatología"],[1,"Cristian","Cirugía"]]:
    pacientes1.put(elem)

e8.printCola(pacientes1)
print(n_pacientes_urgentes(pacientes1))
e8.printCola(pacientes1)
print(n_pacientes_urgentes(Cola()))
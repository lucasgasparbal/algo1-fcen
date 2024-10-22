from numpy import random

## 1

def lista_estudiantes()->list[str]:
    nombre:str = input("Ingrese los nombres de los estudiantes. Escriba 'listo' o nada para terminar.\n")
    estudiantes:list[str] = []
    while (not (nombre == "listo" or nombre == "")):

        estudiantes.append(nombre)
        nombre = input("Ingrese nombre: ")
    
    return estudiantes

# print(lista_estudiantes())

## 2

def historial_monedero()->list[tuple[str,float]]:
    modo_input:str = input("Elija cargar ('C') o descontar ('D') escriba 'X' para terminar.\n")

    historial:list[tuple[str,float]] = []
    while modo_input != "X":
        if(modo_input == "C" or modo_input == "D"):
            monto:float = input("Ingrese el monto: ")
            historial.append((modo_input,monto))
        modo_input = input("Elija tipo de acción (carga 'C' o descuento 'D'). 'X' para terminar.\n")
    
    return historial

# print(historial_monedero())

## 3

def siete_y_medio()->list[int]:
    mazo:list[int] = [1,2,3,4,5,6,7,10,11,12]
    for i in range(4):
        mazo *= 4

    carta_elegida:int = int(random.choice(mazo))
    historial: list[int] = [carta_elegida]

    total:float = 0

    if carta_elegida in [10,11,12]:
            total += 0.5
    else:
            total += float(carta_elegida)
    
    mazo.remove(carta_elegida)
    peticion:str = input("Usted tiene la carta: '"+str(carta_elegida)+ "' Escriba 'carta' para pedir una carta o cualquier otra cosa para plantarse.\n")
    
    while(peticion == "carta"):
        carta_elegida = int(random.choice(mazo))
        mazo.remove(carta_elegida)
        if carta_elegida in [10,11,12]:
            total += 0.5
        else:
            total += float(carta_elegida)
        
        historial.append(carta_elegida)
        if( total > 7.5):
            print("Usted perdió :-(.")
            peticion = ""
        else:
            peticion = input("Su nueva carta fue: '"+ str(carta_elegida) + "' Si quiere pedir una carta escriba 'carta' si no escriba cualquier otra cosa para plantarse. \n ")
    
    if(total == 7.5):
        print("Usted ganó! (°_°)b\n")
    else:
         print("Su total fue: "+str(total))

    return historial

# print(siete_y_medio())

def preguntar_contraseña():
         
    contrasenia:str = input("Ingrese su contraseña para verificar su nivel de seguridad. Para salir del programa no ingrese nada.\n")

    while(contrasenia != ""):
         print("el nivel de seguridad de su contraseña es: "+fortaleza_contraseña(contrasenia)+"\n")

         contrasenia = input("Ingrese otra contraseña para seguir probando. no escriba nada para terminar el programa.\n")




def fortaleza_contraseña(contrasenia:str)->str:
     
     if len(contrasenia) < 5:
          return "ROJA"
     
     minus:bool = False
     mayus:bool = False
     numero:bool = False

     for letra in contrasenia:
          if "a" <= letra and letra <= "z":
               minus = True
          elif "A" <= letra and letra <= "Z":
               mayus = True
          elif "0" <= letra and letra <= "9":
               numero = True

     if len(contrasenia) > 8 and minus and mayus and numero:
          return "VERDE"
     else:
          return "AMARILLO"
     

# preguntar_contraseña()     



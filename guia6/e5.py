def devolver_doble_si_es_par(num:int)->int:

    if(num % 2 == 0):
        return num*2
    else:
        return num
    
# print(devolver_doble_si_es_par(6))
# print(devolver_doble_si_es_par(7))

def devolver_valor_si_es_par_sino_el_que_sigue(numero:int) -> int:
    if(numero % 2 == 0):
        return numero
    
    if(numero % 2 != 0 ):
        return numero+1
    

# print(devolver_valor_si_es_par_sino_el_que_sigue(4))
# print(devolver_valor_si_es_par_sino_el_que_sigue(13))

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(n:int)->int:
    if(n % 9 == 0):
        return n*3
    elif (n % 3 == 0):
        return n*2
    else:
        return n
    
# print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(18))
# print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(15))
# print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(16))

def lindo_nombre(nombre:str)->str:
    if(len(nombre) >= 5):
        return "Tu nombre tiene muchas letras!"
    else:
        return "Tu nombre tiene menos de 5 caracteres"
    
# print(lindo_nombre("alejandro"))
# print(lindo_nombre("juan"))


def elRango(n:int):
    if(n <5):
        print("menor a 5")
    elif(10 <= n and n <= 20):
        print("entre 10 y 20")
    elif( n > 20):
        print("mayor a 20")

# elRango(3)
# elRango(15)
# elRango(24)

def trabaja(sexo:str,edad:int):
    if edad < 18 or (sexo == "F" and edad >= 60) or (sexo == "M" and edad >= 65):
        print("Anda de vacaciones")
    else:
        print("Te toca trabajar")

# trabaja("F",6)
# trabaja("M",15)
# trabaja("F",60)
# trabaja("F",72)
# trabaja("M",65)
# trabaja("M",78)
# trabaja("M",45)
# trabaja("F",23)
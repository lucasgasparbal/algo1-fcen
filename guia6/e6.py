

def imprimir_1_a_10():

    num:int = 1
    while(num <= 10):
        print(num)
        num +=1

# imprimir_1_a_10()
        
def imprimir_pares_10_a_40():
    
    num:int = 10

    while(num <= 40):
        if(num % 2 == 0):
            print(num)
        num += 1

# imprimir_pares_10_a_40()

def imprimir_eco_10():
    
    contador:int = 1
    while(contador <= 10):
        print("eco")
        contador +=1


# imprimir_eco_10()


def cuenta_regresiva(conteo:int):

    while(conteo >= 1):
        print(conteo)
        conteo -= 1
    
    print("Despegue")


# cuenta_regresiva(10)
# cuenta_regresiva(25)

def viaje_en_el_tiempo(desde:int,hasta:int):

    while(desde >= hasta):
        print("Viajó un año al pasado, estamos en el año: " +str(desde))
        desde -= 1


# viaje_en_el_tiempo(2024,2012)
# viaje_en_el_tiempo(2019,2016)

def hasta_Aristoteles(desde:int):

    while(desde >= -384):
        print("Viajó un año al pasado, estamos en el año: " +str(desde))
        desde -= 20
    print("Viajó un año al pasado, estamos en el año: " +str(desde))


hasta_Aristoteles(1994)


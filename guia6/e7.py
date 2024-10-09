
def imprimir_1_a_10():

    for n in range(1,11,1):
        print(n)


#imprimir_1_a_10()
        
def imprimir_pares_10_a_40():
    

    for num in range(10,41,1):
        if(num % 2 == 0):
            print(num)

#imprimir_pares_10_a_40()

def imprimir_eco_10():
    
    for num in range(0,10,1):
        print("eco")


#imprimir_eco_10()


def cuenta_regresiva(conteo:int):

    for n in range(conteo,0,-1):
        print(n)
    
    print("Despegue")


# cuenta_regresiva(10)
# cuenta_regresiva(25)

def viaje_en_el_tiempo(desde:int,hasta:int):

    for n in range(desde,hasta-1,-1):
        print("Viajó un año al pasado, estamos en el año: " +str(n))

# viaje_en_el_tiempo(2024,2012)
# viaje_en_el_tiempo(2019,2016)

def hasta_Aristoteles(desde:int):

    for n in range(desde,-384-20,-20):
        print("Viajó 20 años al pasado, estamos en el año: " +str(n))
    print("Solo se que no se nada")

hasta_Aristoteles(2024)
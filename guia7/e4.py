def saldoResultado(historial:list[tuple[str,float]])->float:
    saldo:float = 0

    for operacion in historial:
        saldo += traducirOperacion(operacion)

    return saldo


def traducirOperacion(operacion:tuple[str,float])->float:
    
    signo:float = 0

    if operacion[0] == "I":
        signo = 1
    elif operacion[0] == "R":
        signo = -1
    
    return signo*operacion[1]


# print(saldoResultado([("I",2000),("R",20),("R",1000),("I",300)]))
# print(saldoResultado([("I",20000),("R",15000),("R",1000),("I",300000),("R",400000)]))      


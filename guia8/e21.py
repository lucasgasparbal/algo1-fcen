
##1

def contar_lineas(nombre_archivo:str)->int:
    archivo = open(nombre_archivo,"r",encoding="utf-8")

    contador:int = 0
    for line in archivo:
        contador += 1

    archivo.close()
    return contador


# print(contar_lineas("e18.txt"))


##2

def existe_palabra(palabra:str, nombre_archivo:str)->bool:
    archivo = open(nombre_archivo,"r",encoding="utf-8")

    for line in archivo:
        tokens:list[str] = line.split()
        for token in tokens:
            if token == palabra:
                return True
    
    archivo.close()
    return False

# print(existe_palabra("moneda","e18.txt"))

##3

def cantidad_apariciones(nombre_archivo:str, palabra:str)->int:
    archivo = open(nombre_archivo,"r",encoding="utf-8")

    cantidad:int = 0
    for line in archivo:
        tokens:list[str] = line.split()
        for token in tokens:
            if token == palabra:
                cantidad += 1
    
    archivo.close()
    return cantidad


# print(cantidad_apariciones("e18.txt","era"))
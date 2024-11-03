def agrupar_por_longitud(nombre_archivo:str)->dict[str,float]:
    archivo = open(nombre_archivo,"r")

    contenido:str = archivo.read()

    tokens:list[str] = contenido.split()

    res:dict[str,float] = {}
    for token in tokens:
        longitud:int = len(token)

        if not pertenece(res.keys(),longitud):
            res[len(token)] = 0

        res[len(token)] += 1
    
    archivo.close()

    return res

    

def pertenece(l:list,x)->bool:
    for elem in l:
        if x == elem:
            return True

    return False


# print(agrupar_por_longitud("e16.txt"))
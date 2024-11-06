def agrupar_por_longitud(nombre_archivo:str)->dict[int,int]:
    archivo:TextIO  = open(nombre_archivo,"r")

    contenido:str = archivo.read()

    tokens:list[str] = tokenizar(contenido)

    res:dict[int,int] = {}
    for token in tokens:
        longitud:int = len(token)

        if not pertenece(res.keys(),longitud):
            res[len(token)] = 0

        res[len(token)] += 1
    
    archivo.close()

    return res


def tokenizar(texto:str) -> list[str]:
    res:list[str] = []
    token:str = ""
    for char in texto:
        if char == " " or char =="\n" or char =="\t":
            if len(token) > 0:
                res.append(token)
            token = ""
        else:
            token += char
    
    if len(token) > 0:
        res.append(token)
    
    return res

def pertenece(l:list,x)->bool:
    for elem in l:
        if x == elem:
            return True

    return False


# print(agrupar_por_longitud("e16.txt"))
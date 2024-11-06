def clonar_sin_comentarios(nombre_archivo:str):
    archivo:TextIO = open(nombre_archivo,"r",encoding="utf-8")

    clon:TextIO = open(nombre_archivo+"_sin_comentarios.txt","w",encoding="utf-8")

    for line in archivo.readlines():
        if not es_comentario(line):
            clon.write(line)

    
    archivo.close()
    clon.close()

def es_comentario(linea:str)->bool:
    for char in linea:
        if char == "#":
            return True
        if char != " ":
            return False
    return False
        
# clonar_sin_comentarios("e15.py")

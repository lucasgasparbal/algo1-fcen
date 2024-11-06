
def agregar_frase_al_final(nombre_archivo:str, frase:str):
    archivo:TextIO = open(nombre_archivo,"r",encoding="utf-8")

    texto:str = ""
    for line in archivo.readlines():
        texto += line
    
    archivo.close()

    texto += "\n"+frase

    archivo = open(nombre_archivo,"w",encoding="utf-8")

    archivo.write(texto)
    archivo.close()

    

agregar_frase_al_final("e24.txt","agregué esta frase con la función del problema")
def agregar_frase_al_principio(nombre_archivo:str,frase:str):
    archivo = open(nombre_archivo,"r",encoding="utf-8")
    texto:str = frase + "\n"
    
    for line in archivo:
        texto += line

    archivo.close()

    archivo = open(nombre_archivo,"w",encoding="utf-8")

    archivo.write(texto)

    archivo.close()


# agregar_frase_al_principio("e25.txt","Esta frase fue agregada con la función agregar_frase_al_principio del ejercicio 25 de la guía 8")
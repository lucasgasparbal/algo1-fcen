import e16

def la_palabra_mas_frecuente(nombre_archivo:str)->tuple[str,int]:

    archivo = open(nombre_archivo,"r",encoding="utf-8")

    contenido = archivo.read()

    tokens:list[str] = contenido.split()

    palabras_apariciones:dict[str,int] = {}
    for token in tokens:
        if not e16.pertenece(palabras_apariciones.keys(),token):
            palabras_apariciones[token] = 1
        else:
            palabras_apariciones[token] += 1
    
    palabra_mas_frecuente:str = ""
    palabras_apariciones[palabra_mas_frecuente] = 0
    for key in palabras_apariciones.keys():
        if  palabras_apariciones[palabra_mas_frecuente] < palabras_apariciones[key]:
            palabra_mas_frecuente = key
    
    return [palabra_mas_frecuente,palabras_apariciones[palabra_mas_frecuente]]


print(la_palabra_mas_frecuente("e18.txt"))

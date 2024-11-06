def listar_palabras_de_archivo(nombre_archivo:str)->list:
    archivo:BufferedRandom = open(nombre_archivo,mode="b+r")
    bytes = archivo.read()
    legibles:list[str] = []
    legible:str =""
    for byte in bytes:
        posible_char:chr = chr(byte)
        if es_caracter_valido(posible_char):
            legible += posible_char
        else:
            if len(legible) >= 5:
                legibles.append(legible)
            legible = ""


    archivo.close()

    return legibles

def es_caracter_valido(posible_char:str)->bool:
    return ("0" <= posible_char and posible_char <= "9") or ("A" <= posible_char and posible_char <= "Z") or ("a" <= posible_char and posible_char <= "z") or posible_char == " " or posible_char == "_"



# print(listar_palabras_de_archivo("e25.txt"))
# print(listar_palabras_de_archivo("socratico.png"))
# print(listar_palabras_de_archivo("mgs.mp3"))
# print(listar_palabras_de_archivo("unknown.7z"))
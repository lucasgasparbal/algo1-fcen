def calcular_promedio_por_estudiantes(nombre_archivo_notas:str,nombre_archivo_promedios:str):
    archivo_notas = open(nombre_archivo_notas,"r")

    libretas:list[str] = []

    for line in archivo_notas:
        tokens = line.split(",")
        if not pertenece(tokens[0],libretas):
            libretas.append(tokens[0])

    archivo_notas.close()
    promedios:dict[str,float] ={}

    for libreta in libretas:
        promedios[libreta] = promedio_estudiante(nombre_archivo_notas,libreta)
    

    archivo_promedios = open(nombre_archivo_promedios+".csv","w")

    for libreta in promedios.keys():
        archivo_promedios.write(libreta+","+str(promedios[libreta])+"\n")

    archivo_promedios.close()

def pertenece(x,lista:list)->bool:
    for elem in lista:
        if x == elem:
            return True
    
    return False



def promedio_estudiante(nombre_archivo_notas:str, lu:str)->float:
    archivo_notas = open(nombre_archivo_notas,"r")

    suma_notas:float = 0
    cant_notas:int = 0
    for line in archivo_notas:
        tokens = line.split(",")
        if tokens[0] == lu:
            suma_notas += float(tokens[3])
            cant_notas += 1

    
    archivo_notas.close()

    return suma_notas / cant_notas


calcular_promedio_por_estudiantes("e27.csv","e27promedios")
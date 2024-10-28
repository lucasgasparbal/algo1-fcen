
def calcular_promedio_por_estudiante(notas:list[tuple[str,float]])->dict[str,float]:
    res:dict[str,float] = {}
    estudiantes_notas:dict[str,list[float]] = {}
    for tupla in notas:

        if not tupla[0] in estudiantes_notas:
            estudiantes_notas[tupla[0]] = []
        
        estudiantes_notas[tupla[0]].append(tupla[1])
    
    for nombre in estudiantes_notas.keys():
        res[nombre] = promedio(estudiantes_notas[nombre])

    return res

    
def promedio(l:list[float])->float:
    sum:float = 0
    for num in l:
        sum += num
    
    return sum / len(l)


# notas = [("a",6.54),("b",8),("c",3),("a",4.46),("c",10),("b",8),("a",10),("a",7)]

# print(calcular_promedio_por_estudiante(notas))
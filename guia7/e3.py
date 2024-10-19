
def resultadosMateria(notas:list[int])->int:
    sum:int = 0
    for nota in notas:
        if nota < 4:
            return 3
        sum += nota

    promedio:float = sum / len(notas)

    if(promedio >= 7):
        return 1
    else:
        return 2


print(resultadosMateria([10,10]))
print(resultadosMateria([7]))
print(resultadosMateria([4,4,4,4]))
print(resultadosMateria([3]))
print(resultadosMateria([10,10,10,10,10,3]))
print(resultadosMateria([3,3,3,7,10,3,3]))
print(resultadosMateria([6,9,10,10]))


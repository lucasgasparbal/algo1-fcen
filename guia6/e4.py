
def peso_pino(metros:int)->int:

    centimetros:int = metros*100

    peso:int = min(300,centimetros)*3 + max(0,centimetros-300)*2

    return peso

# print(peso_pino(5))
# print(peso_pino(2))


def es_peso_util(peso:int)->bool:
    return (400 <= peso and peso <= 1000)

# print(es_peso_util(400))
# print(es_peso_util(1000))
# print(es_peso_util(700))
# print(es_peso_util(2600))

def sirve_pino(altura:int)->bool:
    return es_peso_util(peso_pino(altura))


print(sirve_pino(2))
print(sirve_pino(1))
print(sirve_pino(3))
print(sirve_pino(5))




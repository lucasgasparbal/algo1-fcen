def piramide_de_numeros(n:int):

    for i in range(1,n+1,1):
        numeros:str = ""
        for j in range(0,(n+1)-i,1):
            numeros += " "
        for j in range(1,i+1,1):
             numeros += str(j)
        for j in range(i-1,0,-1):
            numeros += str(j)     

        print(numeros)


piramide_de_numeros(4)

piramide_de_numeros(1)

# piramide_de_numeros(2)

piramide_de_numeros(9)
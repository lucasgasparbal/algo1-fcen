from queue import LifoQueue as Pila

def evaluar_expresion(s:str)->float:
    tokens:list[str] = s.split()

    operandos:Pila[str] = Pila()
    for token in tokens:
        if token == "+" or token == "-" or token == "*" or token == "/":
            resultado:float = realizar_operacion(operandos.get(),operandos.get(),token)
            operandos.put(resultado)
        else:
            operandos.put(float(token))

    
    return operandos.get()


def realizar_operacion(operando2:float,operando1:float,tokenOperacion:str)->bool:
    if tokenOperacion == "+":
        return operando1 + operando2
    elif tokenOperacion =="-":
        return operando1 - operando2
    elif tokenOperacion == "*":
        return operando1*operando2
    elif tokenOperacion == "/":
        return operando1/operando2
    
        
# print(evaluar_expresion("3 4 + 5 * 2 -"))
# print(evaluar_expresion("4 5 + 3 /"))            


def agregar_producto(inventario:dict[str,dict[str,float | int]],nombre:str, precio:float,cantidad:int):
    inventario[nombre]={}

    inventario[nombre]["precio"] = precio
    inventario[nombre]["cantidad"] = cantidad


def actualizar_stock(inventario:dict[str,dict[str,float | int]],nombre:str,cantidad:int):
    inventario[nombre]["cantidad"] += cantidad


def actualizar_precios(inventario:dict[str,dict[str,float | int]],nombre:str,precio:float):
    inventario[nombre]["precio"] = precio


def calcular_valor_inventario(inventario:dict[str,dict[str, float | int]])->float:
    valor_total:float = 0
    for producto in inventario.keys():
        valor_total += (inventario[producto]["precio"])*float(inventario[producto]["cantidad"])
    
    return valor_total


# inventario = {}
# agregar_producto(inventario, "Camisa", 20.0, 50)
# agregar_producto(inventario, "Pantalon", 30.0, 30)
# actualizar_stock(inventario, "Camisa", 10)
# valor_total = calcular_valor_inventario(inventario)
# print("Valor total del inventario:", valor_total)
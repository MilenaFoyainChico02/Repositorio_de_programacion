#definimos la funcion
def calcular_porcentaje (precio, descuento):
    prom =  (precio * descuento)/100
    return prom # retorno
con = 0
resul = input("Precio del producto:")
if resul == "": # caso contrario si es igual a vacio
    print("solo se debe ingresar valores numericos") #imprime
else:
    result = input("ingresar el porcentaje de descuento del producto:")
    if result == "":
        print("solo se debe ingresar valores numericos")
    else:
        con = calcular_porcentaje (float(resul), float(result))
print(con)
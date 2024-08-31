def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)
    return None


# Definición de la matriz 3x3
matriz = [
    [18, 21, 30],
    [4, 58, 62],
    [75, 83, 99]
]

# Valor a buscar
valor = 58

# Buscar el valor en la matriz
resultado = buscar_valor(matriz, valor)

# Mostrar el resultado
if resultado:
    print(f"El valor {valor} se encontró en la posición: {resultado}")
else:
    print(f"El valor {valor} no se encontró en la matriz.")


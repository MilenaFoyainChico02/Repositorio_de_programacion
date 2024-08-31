def bubble_sort(fila):

    n = len(fila)
    for i in range(n):
        # La última i posiciones ya están ordenadas
        for j in range(0, n - i - 1):
            # Si el elemento actual es mayor que el siguiente, intercambiarlos
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]


def ordenar_fila(matriz, fila_index):

    if 0 <= fila_index < len(matriz):
        bubble_sort(matriz[fila_index])
    else:
        print("Índice de fila fuera de rango.")


# Definición de la matriz 3x3
matriz = [
    [9, 3, 5],
    [7, 2, 6],
    [4, 8, 1]
]

# Mostrar la matriz original
print("Matriz Original:")
for fila in matriz:
    print(fila)

# Índice de la fila a ordenar (por ejemplo, la fila 1)
fila_en_orden = 1

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la Fila Ordenada:")
for fila in matriz:
    print(fila)

# matriz 3x4x7
# Datos de temperaturas
arreglo = [
    [ # Guayaquil
        [30, 20, 40, 26, 23, 36, 33], # Semana 1
        [21, 29, 42, 32, 25, 34, 31], # Semana 2
        [22, 27, 24, 35, 41, 28, 36], # Semana 3
        [37, 21, 33, 38, 40, 25, 35]  # Semana 4
    ],
    [ # Puyo
        [20, 28, 15, 18, 21, 13, 31], # Semana 1
        [29, 19, 24, 32, 25, 17, 28], # Semana 2
        [15, 30, 23, 13, 26, 21, 30], # Semana 3
        [33, 24, 16, 12, 11, 10, 23]  # Semana 4
    ],
    [ # Lago Agrio
        [40, 39, 33, 34, 29, 38, 35], # Semana 1
        [41, 29, 39, 33, 28, 22, 42], # Semana 2
        [38, 33, 39, 40, 44, 27, 35], # Semana 3
        [35, 40, 45, 39, 25, 30, 31]  # Semana 4
    ]
]

# Nombres de las ciudades para referencia
ciudades = ["Guayaquil", "Puyo", "Lago Agrio"]

# se calcula el promedio de temperaturas para cada semana en cada ciudad
for i, ciudad in enumerate(ciudades):
    print(f"Temperaturas para {ciudad}:")
    for semana in range(4):  # Hay 4 semanas
        temperaturas_semana = arreglo[i][semana]
        promedio = sum(temperaturas_semana) / len(temperaturas_semana)
        print(f"  Promedio de semana {semana + 1}: {promedio:.2f}")
    print()  # Línea en blanco entre ciudades
# se calcula y muestra el promedio de temperaturas para cada ciudad
for i, ciudad in enumerate(ciudades):
    temperaturas_totales = []

    # se recorre todas las semanas para sumar todas las temperaturas
    for semana in arreglo[i]:
        temperaturas_totales.extend(semana)

    promedio_total = sum(temperaturas_totales) / len(temperaturas_totales)
    print(f"Promedio de temperaturas para {ciudad}: {promedio_total:.2f}")

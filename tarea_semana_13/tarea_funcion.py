arreglo=[
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


def calcular_temperatura_promedio(datos, ciudad, semana_inicio, semana_fin):
    """
    Calcula la temperatura promedio de una ciudad durante un período de semanas.

    datos: lista de listas anidadas con los datos de temperaturas.
    ciudad: indice de la ciudad (0 para Guayaquil, 1 para Puyo, 2 para Lago Agrio).
    semana_inicio: indice de la semana inicial (0 para Semana 1).
    semana_fin: indice de la semana final (0 para Semana 4).
    return: temperatura promedio durante el período especificado.
    """
    # para verificar que el indice de las semanas estén dentro del rango valido
    if ciudad < 0 or ciudad >= len(datos):
        raise ValueError("Índice de ciudad fuera de rango")
    # Verificar que los indices de las semanas estén dentro del rango válido
    if semana_inicio < 0 or semana_fin >= len(datos[ciudad]):
        raise ValueError("indice de semana fuera de rango")
    # para verificar que la semana de inicio no sea mayor que la semana de fin
    if semana_inicio > semana_fin:
        raise ValueError("Semana de inicio no puede ser mayor que semana de fin")
    # lista para almacenar todas las temperaturas del período especificado
    temperaturas = []

    # Iterar sobre las semanas en el rango especificado
    for semana in range(semana_inicio, semana_fin + 1):
        temperaturas.extend(datos[ciudad][semana])

    # Calcular y devolver el promedio
    promedio = sum(temperaturas) / len(temperaturas) if temperaturas else 0
    return promedio

#cálculo de la temperatura promedio para Guayaquil (ciudad 0) de la Semana 1 a la Semana 3
promedio_guayaquil = calcular_temperatura_promedio(arreglo, 0, 0, 2)
print(f"Temperatura promedio en Guayaquil desde la Semana 1 hasta la Semana 3: {promedio_guayaquil:.2f}")

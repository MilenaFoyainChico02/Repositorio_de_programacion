# iniciamos creando un archivo de texto
file = open('my_notes.txt', 'w')
# aqui almacenamos las notas del archivo de texto creado anteriormente
file.write("Pon tu mirada en las cosas de arriba, no en las de la tierra Colosenses 3:2.\n")
file.write("Todo esfuerzo tiene su recompensa, pero quedarse en las palabras solamente, lleva a la pobreza Proverbios 14:23.\n")
file.write("En tu mente puede verse complicado, pero en las manos de Dios tiene solución 1Pedro 5:7.\n")
file.close() # cerramos

# procedemos a abrir el archivo para poder leerlo
file = open('my_notes.txt', 'r')
line = file.readline()
# Creamos un bucle while para asegurar que el programa continúe leyendo y mostrando líneas hasta que line sea una cadena vacía
while line:
    print(line.strip())  # strip() elimina espacios y saltos de línea extra
    line = file.readline()  # Lee la siguiente línea
file.close()

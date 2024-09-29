# diccionario
informacion_personal = {"nombre" :"Manuel" , "apellido" :"Rodriguez", "edad":"30", "ciudad" : "santo domingo"}

# Cambiar la ciudad
informacion_personal["ciudad"] = "Santiago de los caballeros"

# Cambiar la profesión
informacion_personal["profesion"]= "licenciado en educacion fisica"
# Verificar si la información personal telefono existe, sino existe se debe de agregar el número de telefono

if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+1 (829) 6784093"

   # Eliminamos la clave edad
del informacion_personal["edad"]

# Imprimir
print(informacion_personal)
# Crear una lista con los nombres de 10 estudiantes.
# Solicitar al usuario que ingrese un nombre a buscar.
# Indicar si el nombre se encuentra en la lista.
# Mostrar la posición en la que aparece.
# Si no se encuentra, informar que no está en la lista

estudiantes = [
    "Juan",
    "Pedro",
    "Ana",
    "Lucia",
    "Martin",
    "Sofia",
    "Carlos",
    "Valentina",
    "Federico",
    "Camila"
]

nombre = input("Ingrese el nombre que desea buscar: ")

if nombre in estudiantes:

    posicion = estudiantes.index(nombre)

    print("El estudiante se encuentra en la lista.")
    print("Su posición es:", posicion)

else:

    print("El estudiante no se encuentra en la lista.")
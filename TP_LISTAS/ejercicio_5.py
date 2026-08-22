# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# Mostrar la lista final actualizada.

estudiantes = ["juan", "pedro", "ana", "lucia", "martin", "sofia", "carlos", "valentina"]

print("Lista de Estudiantes")
print(estudiantes)

opcion = input("¿Qué desea hacer? 1 - Agregar estudiante / 2 - Eliminar estudiante: ")

while opcion not in ["1", "2"]:
    print("Opcion incorrecta! Elija una opcion valida")
    opcion = input("¿Qué desea hacer? 1 - Agregar estudiante / 2 - Eliminar estudiante: ")

if opcion == "1":
    agregarEstudiante = input("Ingrese el estudiante que desea agregar: ").lower()
    if agregarEstudiante == "":
        print("Ingrese una opcion valida!")
    else:
        estudiantes.append(agregarEstudiante)
        print("Estudiante agregado correctamente")
elif opcion == "2":
    eliminarEstudiante = input("Que estudiante desea eliminar?").lower()
    
    while eliminarEstudiante not in estudiantes:
        print("El estudiante no existe!")
        eliminarEstudiante = input("Ingrese un estudiante valido: ")
    
    estudiantes.remove(eliminarEstudiante)
    print("Estudiante eliminado con exito!")

print("Lista de estudiantes actualizada: ")
print(estudiantes)
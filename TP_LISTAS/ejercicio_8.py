# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# Mostrar el promedio de cada estudiante.
# Mostrar el promedio de cada materia.


notas = [
    [7, 8, 9],
    [6, 7, 8],
    [10, 9, 8],
    [5, 6, 7],
    [8, 9, 10]
]

for i in range(len(notas)):
    suma = 0

    for j in range(len(notas[i])):
        suma += notas[i][j]

    promedio = suma / len(notas[i])
    print(f"El promedio del estudiante {i + 1} es: " , promedio)

print("////////////////////////////////////////")

for j in range(len(notas[0])):
    sumaMateria = 0
    for i in range(len(notas)):
        sumaMateria += notas[i][j]
    promedioMateria = sumaMateria / len(notas)
    print(f"El promedio de la materia {j + 1} es: " , promedioMateria)
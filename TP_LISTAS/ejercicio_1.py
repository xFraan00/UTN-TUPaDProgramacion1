# 1) Crear una lista con las notas de 10 estudiantes.
# Mostrar la lista completa.
# Calcular y mostrar el promedio.
# Indicar la nota más alta y la más baja

notas = [10,6.6,8,4.6,7,4,9.4,2,7.5,10]

print("Notas de los alumnos: ")
print(notas)

sumaTotal = 0

for i in range (len(notas)):
    sumaTotal += notas[i]
print("El promedio total es: " , sumaTotal / len(notas))
print("La nota mas alta es: ", max(notas))
print("La nota mas baja es: ", min(notas))
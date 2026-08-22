# Dada una lista con valores repetidos:
# datos = [1,3,5,3,7,1,9,5,3]
# Crear una nueva lista sin elementos repetidos.
# Mostrar el resultado.

datos = [1,3,5,3,7,1,9,5,3]

datosSinRepetir = []

for i in range(len(datos)):
    if datos[i] not in datosSinRepetir:
        datosSinRepetir.append(datos[i])

print("Datos sin repetir: ")
print(datosSinRepetir)
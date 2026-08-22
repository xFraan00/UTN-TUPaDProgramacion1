# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de
# una semana.
# Calcular el promedio de las mínimas y el de las máximas.
# Mostrar en qué día se registró la mayor amplitud térmica.

temperaturas = [
    [10, 20],
    [8, 18],
    [10, 22],
    [15, 18],
    [6, 8],
    [22, 26],
    [10, 14]
]

sumaMinimas = 0
sumaMaximas = 0

for i in range(len(temperaturas)):
    sumaMinimas += temperaturas[i][0]
    sumaMaximas += temperaturas[i][1]

promedioMinimas = sumaMinimas / len(temperaturas)
promedioMaximas = sumaMaximas / len(temperaturas)

print("El promedio de las temperaturas maximas es: " , promedioMaximas)
print("El promedio de las temperaturas minimas es: " , promedioMinimas)

mayorAmplitud = 0
diaMayorAmplitud = 0

for i in range(len(temperaturas)):
    amplitud = temperaturas[i][1] - temperaturas[i][0] 
    if amplitud > mayorAmplitud:
        mayorAmplitud = amplitud
        diaMayorAmplitud = i

print("Mayor amplitud termica: ")
print(mayorAmplitud)
print("Dia con la mayor amplitud termica: ")
print(diaMayorAmplitud + 1)

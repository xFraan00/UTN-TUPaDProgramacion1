# Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha
# (el último pasa a ser el primero).

numeros = [10, 20, 30, 40, 50, 60, 70]

ultimo = numeros[-1]

for i in range(5, -1, -1):
    numeros[i + 1] = numeros[i]
numeros[0] = ultimo

print(numeros)

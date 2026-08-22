# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# Crear una lista con los pares y otra con los impares.
# Mostrar cuántos números tiene cada lista.

import random 

numeros = []
pares = []
impares = []

for i in range(15):
   numero = random.randint(1, 100)
   numeros.append(numero)
print("La lista de numeros es: ")
print(numeros)

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
      pares.append(numeros[i])
    else:
      impares.append(numeros[i])

print("La lista de numeros pares es: ")
print(pares)
print("La lista de numeros impares es: ")
print(impares)

print("La cantidad de numeros que tiene la lista par es: " , len(pares))
print("La cantidad de numeros que tiene la lista impar es: " , len(impares))
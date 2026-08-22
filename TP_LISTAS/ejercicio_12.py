# Pedir al usuario que ingrese 8 números enteros y almacenarlos en una lista.
# Mostrar la lista original.
# Mostrar la lista ordenada de menor a mayor.
# Mostrar la lista ordenada de mayor a menor.
# Investigar el uso de sorted() y del parámetro reverse

numeros = []

for i in range(8):

    numero = input("Ingrese un número entero: ")

    while not numero.isdigit():
        numero = input("Ingrese un número entero válido: ")

    numero = int(numero)

    numeros.append(numero)


print("Lista original:")
print(numeros)


listaOrdenada = sorted(numeros)

print("Lista ordenada de menor a mayor:")
print(listaOrdenada)


listaOrdenadaMayor = sorted(numeros, reverse=True)

print("Lista ordenada de mayor a menor:")
print(listaOrdenadaMayor)


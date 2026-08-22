# 2) Pedir al usuario que cargue 5 productos en una lista.
# Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# Preguntar al usuario qué producto desea eliminar y actualizar la lista.


listaProductos = []

for i in range(5):
    producto = input("Ingrese un producto: ")
    if producto == "":
        print("Error! Ingrese una opcion valida:")
        continue
    listaProductos.append(producto)

print("Lista de Productos sin ordenar")
print(listaProductos)

listaProductosOrdenada = sorted(listaProductos)

print("Lista de productos ordenada")
print(listaProductosOrdenada)

eliminarProducto = input("Que producto desea eliminar? ")

while eliminarProducto not in listaProductos:
    print("El producto no existe!")
    eliminarProducto = input("Ingrese un producto valido: ")

listaProductos.remove(eliminarProducto)
print("El producto a sido eliminado con exito!")
print(listaProductos)
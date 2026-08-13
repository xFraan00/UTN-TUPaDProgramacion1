nombre = input("Ingrese su nombre: ")

while not nombre.isalpha():
    nombre = input("Ingrese un nombre valido: ")

producto_a_comprar = input("Ingrese la cantidad de productos a comprar: ")

while not producto_a_comprar.isdigit():
    producto_a_comprar = input("Ingrese un numero valido: ")

producto_a_comprar = int(producto_a_comprar)

while producto_a_comprar <= 0:
    producto_a_comprar = int(input("Ingrese un numero mayor a 0: "))


total_sin_descuento = 0
total_con_descuento = 0
ahorro_total = 0


for i in range(producto_a_comprar):
    precio = input("Ingrese el precio del producto: ")

    while not precio.isdigit():
        precio = input("Ingrese un precio válido: ")

    precio = int(precio)

    descuento = input("Su producto tiene descuento? s/n: ").lower()

    while descuento != "s" and descuento != "n":
        descuento = input("Ingrese una opcion valida: ").lower()

    precio_con_descuento = precio

    if descuento == "s":
        precio_con_descuento = precio * 0.90

    total_sin_descuento += precio
    total_con_descuento += precio_con_descuento
    ahorro_total += precio - precio_con_descuento


promedio = total_con_descuento / producto_a_comprar


print()
print("Cliente:", nombre)
print("Cantidad de productos:", producto_a_comprar)
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro_total:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")


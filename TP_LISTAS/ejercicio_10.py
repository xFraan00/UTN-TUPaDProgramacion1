# Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# Mostrar el total vendido por cada producto.
# Mostrar el día con mayores ventas totales.
# Indicar cuál fue el producto más vendido en la semana.


ventas = [
    [10, 15, 20, 12, 18, 25, 30],
    [20, 18, 15, 25, 30, 22, 28],
    [12, 10, 15, 18, 20, 16, 22],
    [25, 30, 28, 35, 32, 40, 38]
]

totalesProductos = []

for i in range(len(ventas)):

    totalProducto = 0

    for j in range(len(ventas[i])):
        totalProducto += ventas[i][j]

    totalesProductos.append(totalProducto)

    print("Total vendido del producto", i + 1, ":", totalProducto)


mayorVentaDia = 0
diaMayorVenta = 0

for j in range(len(ventas[0])):

    totalDia = 0

    for i in range(len(ventas)):
        totalDia += ventas[i][j]

    if totalDia > mayorVentaDia:
        mayorVentaDia = totalDia
        diaMayorVenta = j

print("El día con mayores ventas totales fue el día", diaMayorVenta + 1)
print("Ventas totales de ese día:", mayorVentaDia)


mayorProducto = max(totalesProductos)
productoMasVendido = totalesProductos.index(mayorProducto)

print("El producto más vendido fue el producto", productoMasVendido + 1)
print("Total vendido:", mayorProducto)
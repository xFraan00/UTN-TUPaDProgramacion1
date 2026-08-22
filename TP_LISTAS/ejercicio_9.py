# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# Inicializarlo con guiones "-" representando casillas vacías.
# Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# Mostrar el tablero después de cada jugada.

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

jugadas = 0
jugador = "X"
ganador = False

print("Tablero de Ta-Te-Ti")

for fila in tablero:
    print(fila)

while jugadas < 9 and ganador == False:

    print("¡Jugador", jugador, "ingrese su jugada!")

    fila = input("Ingrese la fila (1-3): ")

    while not fila.isdigit() or int(fila) < 1 or int(fila) > 3:
        fila = input("Ingrese una fila válida (1-3): ")

    fila = int(fila)

    columna = input("Ingrese la columna (1-3): ")

    while not columna.isdigit() or int(columna) < 1 or int(columna) > 3:
        columna = input("Ingrese una columna válida (1-3): ")

    columna = int(columna)

    fila = fila - 1
    columna = columna - 1

    while tablero[fila][columna] != "-":

        print("La casilla ya está ocupada. Elija otra.")

        fila = input("Ingrese la fila (1-3): ")

        while not fila.isdigit() or int(fila) < 1 or int(fila) > 3:
            fila = input("Ingrese una fila válida (1-3): ")

        fila = int(fila)

        columna = input("Ingrese la columna (1-3): ")

        while not columna.isdigit() or int(columna) < 1 or int(columna) > 3:
            columna = input("Ingrese una columna válida (1-3): ")

        columna = int(columna)

        fila = fila - 1
        columna = columna - 1

    tablero[fila][columna] = jugador

    print("Tablero actualizado:")

    for fila in tablero:
        print(fila)

    jugadas += 1

    # Comprobar filas
    if tablero[0][0] == tablero[0][1] == tablero[0][2] and tablero[0][0] != "-":
        ganador = True

    elif tablero[1][0] == tablero[1][1] == tablero[1][2] and tablero[1][0] != "-":
        ganador = True

    elif tablero[2][0] == tablero[2][1] == tablero[2][2] and tablero[2][0] != "-":
        ganador = True

    # Comprobar columnas
    elif tablero[0][0] == tablero[1][0] == tablero[2][0] and tablero[0][0] != "-":
        ganador = True

    elif tablero[0][1] == tablero[1][1] == tablero[2][1] and tablero[0][1] != "-":
        ganador = True

    elif tablero[0][2] == tablero[1][2] == tablero[2][2] and tablero[0][2] != "-":
        ganador = True

    # Comprobar diagonales
    elif tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != "-":
        ganador = True

    elif tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != "-":
        ganador = True

    if ganador == True:
        print("¡Ganó el jugador", jugador, "!")

    else:
        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"

if ganador == False:
    print("¡Empate! El tablero está completo.")




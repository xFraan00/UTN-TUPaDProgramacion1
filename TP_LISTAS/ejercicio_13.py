# 13) Dada la siguiente lista de puntajes de un videojuego:
# puntajes = [450, 1200, 875, 990, 300, 1500, 640]
# Mostrar el puntaje más alto y el más bajo.
# Mostrar la lista ordenada de mayor a menor (ranking).
# Indicar en qué posición del ranking se encuentra el puntaje 990.

puntajes = [450, 1200, 875, 990, 300, 1500, 640]

puntajeMayor = max(puntajes)
puntajeMenor = min(puntajes)

print("El puntaje más alto es:", puntajeMayor)
print("El puntaje más bajo es:", puntajeMenor)

ranking = sorted(puntajes, reverse=True)

print("Ranking de mayor a menor:")
print(ranking)

puntajeBuscado = 990

if puntajeBuscado in ranking:

    posicion = ranking.index(puntajeBuscado)

    print("El puntaje 990 se encuentra en la posición:", posicion + 1)

else:

    print("El puntaje 990 no se encuentra en el ranking.")
print("--- BIENVENIDO A LA ARENA ---")


nombre = input("Nombre del Gladiador: ")

while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")


# Estadísticas iniciales

vida_jugador = 100
vida_enemigo = 100

pociones = 3

ataque_pesado = 15
ataque_enemigo = 12

turno_gladiador = True
juego_activo = True


print("\n=== INICIO DEL COMBATE ===")


while juego_activo:

    if vida_jugador <= 0 or vida_enemigo <= 0:
        juego_activo = False


    else:

        if turno_gladiador == True:

            print("\n", nombre, "(HP:", vida_jugador, ") vs Enemigo (HP:", vida_enemigo, ") | Pociones:", pociones)

            print("\nElige acción:")
            print("1. Ataque Pesado")
            print("2. Ráfaga Veloz")
            print("3. Curar")


            opcion = input("Opción: ")


            while not opcion.isdigit():
                print("Error: Ingrese un número válido.")
                opcion = input("Opción: ")


            opcion = int(opcion)


            while opcion < 1 or opcion > 3:
                opcion = int(input("Error: Ingrese una opción entre 1 y 3: "))


            # ATAQUE PESADO

            if opcion == 1:

                daño = ataque_pesado

                if vida_enemigo < 20:

                    daño = ataque_pesado * 1.5
                    print("¡Golpe crítico!")

                vida_enemigo -= daño

                print("¡Atacaste al enemigo por", daño, "puntos de daño!")


            # RAFAGA VELOZ

            elif opcion == 2:

                print("¡Inicias una ráfaga de golpes!")

                for golpe in range(3):

                    vida_enemigo -= 5

                    print("> Golpe conectado por 5 de daño")


            # CURAR

            elif opcion == 3:

                if pociones > 0:

                    vida_jugador += 30
                    pociones -= 1

                    print("Usaste una poción. Recuperaste 30 puntos de vida.")

                    if vida_jugador > 100:
                        vida_jugador = 100

                else:

                    print("¡No quedan pociones!")


            # TURNO ENEMIGO

            if vida_enemigo > 0:

                vida_jugador -= ataque_enemigo

                print("¡El enemigo te atacó por", ataque_enemigo, "puntos de daño!")


            turno_gladiador = True



# FIN DEL JUEGO

print("\n=== FIN DEL COMBATE ===")


if vida_jugador > 0:

    print("¡VICTORIA!", nombre, "ha ganado la batalla.")

else:

    print("DERROTA. Has caído en combate.")
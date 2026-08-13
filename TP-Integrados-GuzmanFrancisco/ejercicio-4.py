energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

racha_forzar = 0


agente = input("Ingrese nombre del agente: ")

while not agente.isalpha():
    agente = input("Nombre inválido. Ingrese nuevamente: ")


while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and alarma == False:

    print("\n--- ESTADO DE LA BOVEDA ---")
    print("Agente:", agente)
    print("Energia:", energia)
    print("Tiempo:", tiempo)
    print("Cerraduras abiertas:", cerraduras_abiertas)
    print("Alarma:", alarma)

    print("\n1- Forzar cerradura")
    print("2- Hackear panel")
    print("3- Descansar")


    opcion = input("Seleccione una opcion: ")

    while not opcion.isdigit():
        opcion = input("Opcion invalida. Ingrese un numero: ")

    opcion = int(opcion)

    while opcion < 1 or opcion > 3:
        opcion = int(input("Ingrese una opcion entre 1 y 3: "))


    # FORZAR CERRADURA
    if opcion == 1:

        energia -= 20
        tiempo -= 2

        racha_forzar += 1


        if racha_forzar == 3:

            print("La cerradura se trabó. Alarma activada.")
            alarma = True

        else:

            if energia < 40:

                riesgo = input("Riesgo de alarma. Ingrese un numero del 1 al 3: ")

                while not riesgo.isdigit():
                    riesgo = input("Ingrese un numero valido: ")

                riesgo = int(riesgo)

                while riesgo < 1 or riesgo > 3:
                    riesgo = int(input("Ingrese un numero entre 1 y 3: "))


                if riesgo == 3:
                    alarma = True
                    print("Alarma activada.")


            if alarma == False:

                cerraduras_abiertas += 1
                print("Cerradura abierta correctamente.")


    # HACKEAR PANEL
    elif opcion == 2:

        energia -= 10
        tiempo -= 3

        racha_forzar = 0

        print("Hackeando panel...")

        for paso in range(4):
            print("Progreso paso", paso + 1)

            codigo_parcial += "A"


        print("Codigo parcial:", codigo_parcial)


        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:

            cerraduras_abiertas += 1
            print("El panel fue hackeado. Cerradura abierta.")



    # DESCANSAR
    elif opcion == 3:

        racha_forzar = 0

        energia += 15

        if energia > 100:
            energia = 100

        tiempo -= 1


        if alarma == True:
            energia -= 10


        print("El agente descanso.")


    # BLOQUEO POR ALARMA
    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        print("Sistema bloqueado por alarma.")
        break



# FIN DEL JUEGO

if cerraduras_abiertas == 3:

    print("\nVICTORIA")
    print("Abriste las 3 cerraduras.")

elif alarma == True:

    print("\nDERROTA")
    print("La alarma bloqueo el sistema.")

elif energia <= 0 or tiempo <= 0:

    print("\nDERROTA")
    print("Te quedaste sin energia o tiempo.")

    
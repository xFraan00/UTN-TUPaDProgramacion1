lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""


operador = input("Ingrese nombre del operador: ")

while not operador.isalpha():
    operador = input("Nombre inválido. Ingrese nuevamente: ")


opcion = 0

while opcion != 5:

    print("\n1- Reservar turno")
    print("2- Cancelar turno")
    print("3- Ver agenda del dia")
    print("4- Ver resumen general")
    print("5- Cerrar sistema")

    opcion = input("Seleccione una opción: ")

    while not opcion.isdigit():
        opcion = input("Opción incorrecta. Ingrese un número: ")

    opcion = int(opcion)

    while opcion < 1 or opcion > 5:
        opcion = int(input("Ingrese una opción entre 1 y 5: "))


    # RESERVAR TURNO
    if opcion == 1:

        dia = input("Seleccione día (1=Lunes, 2=Martes): ")

        paciente = input("Ingrese nombre del paciente: ")

        while not paciente.isalpha():
            paciente = input("Nombre inválido. Ingrese nuevamente: ")


        if dia == "1":

            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("El paciente ya tiene un turno ese día")

            elif lunes1 == "":
                lunes1 = paciente
                print("Turno reservado correctamente")

            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado correctamente")

            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado correctamente")

            elif lunes4 == "":
                lunes4 = paciente
                print("Turno reservado correctamente")

            else:
                print("No hay turnos disponibles para Lunes")


        elif dia == "2":

            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("El paciente ya tiene un turno ese día")

            elif martes1 == "":
                martes1 = paciente
                print("Turno reservado correctamente")

            elif martes2 == "":
                martes2 = paciente
                print("Turno reservado correctamente")

            elif martes3 == "":
                martes3 = paciente
                print("Turno reservado correctamente")

            else:
                print("No hay turnos disponibles para Martes")

        else:
            print("Día inválido")


    # CANCELAR TURNO
    elif opcion == 2:

        dia = input("Seleccione día (1=Lunes, 2=Martes): ")

        paciente = input("Ingrese nombre del paciente: ")

        while not paciente.isalpha():
            paciente = input("Nombre inválido. Ingrese nuevamente: ")


        encontrado = False


        if dia == "1":

            if paciente == lunes1:
                lunes1 = ""
                encontrado = True

            elif paciente == lunes2:
                lunes2 = ""
                encontrado = True

            elif paciente == lunes3:
                lunes3 = ""
                encontrado = True

            elif paciente == lunes4:
                lunes4 = ""
                encontrado = True


        elif dia == "2":

            if paciente == martes1:
                martes1 = ""
                encontrado = True

            elif paciente == martes2:
                martes2 = ""
                encontrado = True

            elif paciente == martes3:
                martes3 = ""
                encontrado = True


        if encontrado:
            print("Turno cancelado")
        else:
            print("Paciente no encontrado")


    # VER AGENDA
    elif opcion == 3:

        dia = input("Seleccione día (1=Lunes, 2=Martes): ")


        if dia == "1":

            print("\nAgenda Lunes:")

            if lunes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", lunes1)

            if lunes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", lunes2)

            if lunes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", lunes3)

            if lunes4 == "":
                print("Turno 4: (libre)")
            else:
                print("Turno 4:", lunes4)


        elif dia == "2":

            print("\nAgenda Martes:")

            if martes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", martes1)

            if martes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", martes2)

            if martes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", martes3)

        else:
            print("Día inválido")


    # RESUMEN GENERAL
    elif opcion == 4:

        ocupados_lunes = 0
        ocupados_martes = 0


        if lunes1 != "":
            ocupados_lunes += 1

        if lunes2 != "":
            ocupados_lunes += 1

        if lunes3 != "":
            ocupados_lunes += 1

        if lunes4 != "":
            ocupados_lunes += 1


        if martes1 != "":
            ocupados_martes += 1

        if martes2 != "":
            ocupados_martes += 1

        if martes3 != "":
            ocupados_martes += 1


        disponibles_lunes = 4 - ocupados_lunes
        disponibles_martes = 3 - ocupados_martes


        print("\nResumen general:")
        print("Lunes - Ocupados:", ocupados_lunes, "Disponibles:", disponibles_lunes)
        print("Martes - Ocupados:", ocupados_martes, "Disponibles:", disponibles_martes)


        if ocupados_lunes > ocupados_martes:
            print("El día con más turnos es Lunes")

        elif ocupados_martes > ocupados_lunes:
            print("El día con más turnos es Martes")

        else:
            print("Ambos días tienen la misma cantidad de turnos")


print("Sistema cerrado")
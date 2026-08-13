usuario_correcto = "alumno"
clave_correcta = "python123"
cantidad_de_intentos = 0

while cantidad_de_intentos < 3:
    print("Ingrese su nombre de usuario: ")
    usuario = input()

    print("Ingrese su contraseña: ")
    clave = input()

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Bienvenido")
        break
    else:
        print("Usuario o contraseña incorrectos")
        cantidad_de_intentos += 1


if cantidad_de_intentos == 3:
    print("Cuenta bloqueada")

else:
    opcion = 0

    while opcion != 4:
        print("\n1- Estado de inscripción")
        print("2- Cambiar clave")
        print("3- Mensaje motivacional")
        print("4- Salir")

        opcion = input("Seleccione una opción: ")

        while not opcion.isdigit():
            opcion = input("Opción incorrecta. Ingrese un número: ")

        opcion = int(opcion)

        while opcion < 1 or opcion > 4:
            opcion = int(input("Ingrese una opción entre 1 y 4: "))

        if opcion == 1:
            print("Inscripto")

        elif opcion == 2:
            print("Cambiar clave")

            nueva_clave = input("Ingrese una nueva contraseña: ")

            while len(nueva_clave) < 6:
                print("La contraseña debe tener mínimo 6 caracteres")
                nueva_clave = input("Ingrese una nueva contraseña: ")

            confirmacion = input("Confirme su contraseña: ")

            while nueva_clave != confirmacion:
                print("Las contraseñas no coinciden")
                confirmacion = input("Confirme su contraseña: ")

            clave_correcta = nueva_clave
            print("Su contraseña se cambió con éxito!")

        elif opcion == 3:
            print("Cada error es una oportunidad para aprender.")

        elif opcion == 4:
            print("Adios")


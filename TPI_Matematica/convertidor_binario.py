opcion = input("Ingrese una opción: 1-Convertir de decimal a binario. 2-Convertir de binario a decimal. 3-Salir. ").strip()

while opcion != "3":

    if opcion == "1":
        numero = input("Ingrese un número decimal: ").strip()
        restos = []

        if numero.isdecimal():
            numero = int(numero)
            print("Es un número válido")

            if numero == 0:
                print("0")
            else:
                while numero > 0:
                    resto = numero % 2
                    restos.append(resto)
                    numero = numero // 2

                print("El numero binario convertido es: ", end="")
                for elemento in reversed(restos):
                    print(elemento, end="")
                print()

        else:
            print("Dato incorrecto")

    elif opcion == "2":
        numero = input("Ingrese un número binario: ").strip()
        valido = True
        resultado = 0
        potencia = len(numero) - 1

        if numero == "":
            valido = False

        for digito in numero:

            if digito != "0" and digito != "1":
                valido = False
            else:
                resultado = resultado + int(digito) * (2 ** potencia)

            potencia = potencia - 1

        if valido:
            print("Dato valido")
            print("El número decimal es:", resultado)
        else:
            print("Dato incorrecto")

    else:
        print("Opción inválida. Ingrese una opción válida.")

    opcion = input("Ingrese una opción: 1-Convertir de decimal a binario. 2-Convertir de binario a decimal. 3-Salir. ").strip()

print("Programa cerrado.")

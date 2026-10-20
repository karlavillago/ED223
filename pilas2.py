pila = []

while True:
    print("\n1. Insertar en pila")
    print("2. Borrar en pila")
    print("3. Listar pila")
    print("4. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        numero = input("Ingresa un numero: ")
        pila.append(numero)

    elif opcion == "2":
        if len(pila) > 0:
            print("Se elimino:", pila.pop())
        else:
            print("La pila esta vacia")

    elif opcion == "3":
        print(pila)

    elif opcion == "4":
        break

    else:
        print("Opcion incorrecta")

    repetir = input("¿Deseas continuar? (s/n): ")
    if repetir != "s":
        break

print("Fin del programa")
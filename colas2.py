from collections import deque

cola = deque()

while True:
    print("\n1. Insertar cola")
    print("2. Borrar en cola")
    print("3. Listar cola")
    print("4. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        numero = input("Ingresa un numero: ")
        cola.append(numero)

    elif opcion == "2":
        if len(cola) > 0:
            print("Se elimino:", cola.popleft())
        else:
            print("La cola esta vacia")

    elif opcion == "3":
        print(list(cola))

    elif opcion == "4":
        break

    else:
        print("Opcion incorrecta")

    repetir =input("¿Deseas continuar? (s/n): ")

    if repetir !="s":
        break

print("Fin del programa")
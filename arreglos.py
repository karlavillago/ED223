#declarar un arreglo
numeros=[10,20,30,40,50]

#para ver un numero en la posicion 2 es el 30
print(numeros[2])

#modificar el numero de la posicion 3 con 15
numeros[3]=15

#y aqui se mando a imprimir
print(numeros)

#como agregar valor al final de un arreglo, con appened
numeros.append(60)
#imprime los numeros
print(numeros)

#eliminar un valor del arreglo con pop en la posicion 1 que es el 20
numeros.pop(1)
print(numeros)

#eliminamos por el valor 30
numeros.remove(30)
print(numeros)

frutas=["mango","manzana","uva","pera"]
frutas.remove("uva")
print(frutas)

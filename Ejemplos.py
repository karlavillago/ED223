Matriz= [
    [1,2,3],
    [4,5,6]
]
print("mostrar la matriz")
for fila in matriz:
    print (fila)

    print("mostrar el 6")
    print(matriz[1][2])

""" SE MUESTRA LA FILA 0 """ 
print(matriz [0])
Matriz[1][1]=8
print(matriz)

""" agregar """
matriz.append([7,8,9])
print(matriz)

""" borrar un valor especifico """
matriz[0].pop(2)
print(matriz)
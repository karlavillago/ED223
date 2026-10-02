""" imprimir numeros  """
numeros= [10, 20, 30, 40, 50]

print(numeros[2])
"""  cambiar numeros desde el indice """
numeros = [10, 20, 30, 40, 50]

numeros[2] = 100

print(numeros)
""" agregar valores al final  """




numeros = [10, 20, 30, 40]
numeros.insert(2, 95)
numeros.extend([50, 67])

print(numeros)
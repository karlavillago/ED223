matriz = [
(73,12,89,21),
(5,61,27,94),
(76,18,80,3)
]

for i in matriz:
  if 80 in i:
   break
print (f" el 80 está en la fila (i)")
for fila in matriz:
  for numero in fila:
   if numero == 80:
     print(f"El 80 está en (fila)")
" crea una pila vacia "
historial = []
historical.append("google.com")
historical.append("youtube.com")
historical.append("github.com")

print("historial:", historial)

"ver el elemento superior"
pagina_actual = historial[2]
print("pagina actual:, pagina_actual")

"despilar/pop"
pagina_salida = historial.pop()
print("saliendo de:", pagina_salida)

print("historial actualizado:", historial)





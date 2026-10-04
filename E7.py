
numeros = [3, 8, 12, 5, 2, 7, 10]

for indice, valor in enumerate(numeros):
	
	print(f"Posicion {indice}: {valor}")

print("La lista con los cuadrados de los numeros pares de la lista anterior es: ")

cuadrados_pares = [i**2 for i in numeros if i % 2 == 0]
print(cuadrados_pares)
print(f"La suma total de sus elementos es: {sum(cuadrados_pares)}")





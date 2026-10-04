import random
print("Adivina el numero del 1 al 20")
numero_random = random.randint(1, 20)

numero_usuario = 0

numero_intentos = 1
while numero_usuario != numero_random:
	
	numero_usuario = int(input("Ingresa tu numero: "))
	
	if numero_usuario > numero_random:
		print("El numero que ingresaste es mayor")
		numero_intentos += 1
		
	elif numero_usuario < numero_random:
		print("El numero que ingresaste es menor")
		numero_intentos +=1
		
	else:
		print("¡Lo adivinaste!")
		print(f"Tu numero de intentos fue:  {numero_intentos}")
	
	
	
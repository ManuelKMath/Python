
def agregar_nota(estudiantes):
		nombre = input("Introduce el nombre del estudiante: ")
		materia = input("Introduce la materia: ").lower()
		nota = float(input("Introduce la nota: "))
		if nombre in estudiantes:
			estudiantes[nombre][materia] = nota
		else:
			estudiantes[nombre] = {materia : nota}
		
		return 

def calcular_promedio(estudiantes):
		nombre = input("Introduce el nombre del estudiante: ")
		if nombre in estudiantes:
			promedio = 0
			for k, materia_y_nota in estudiantes.items():
				if k == nombre:
					for nota in materia_y_nota.values() :
						promedio += nota / len(materia_y_nota)
					print(f"El estudiante {nombre} tiene un promedio de: {promedio}")
		else:
			print(f"El alumno {nombre} no esta registrado.")				
		
		return

print("Calificaciones de Estudiantes")
	
estudiantes = {
    "Juan": {"matematica": 15, "programacion": 18},
    "Maria": {"matematica": 20, "programacion": 19}
}

abierto = True
opcion = 0
while abierto:
	print("1. Agregar o actualizar notas")
	print("2. Calcular promedio")
	print("3. Salir")
	opcion = int(input("¿Cual opcion vas a elegir? "))
	
	if opcion == 1:
		agregar_nota(estudiantes)
		print(" ")
	elif opcion == 2:
		calcular_promedio(estudiantes)
		print(" ")
	elif opcion == 3:
		abierto = False
		print("Saliendo...")
	else:
		print(" ")
		opcion = 0







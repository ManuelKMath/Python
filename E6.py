
Estudiantes = {}
Estudiante_ingresado = 0
Nota_estudiante_ingresado = 0
Promedio_notas = 0
Nota_max = 0
for i in range(3):
	Estudiante_ingresado = input(f"Ingresa el nombre del estudiante {i+1}: ")
	Nota_estudiante_ingresado = float(input(f"Ingresa la nota del estudiante {i+1}: "))
	Promedio_notas += Nota_estudiante_ingresado / 3
	Estudiantes[Estudiante_ingresado] = Nota_estudiante_ingresado
	if Nota_max < Nota_estudiante_ingresado:
		Nota_max = Nota_estudiante_ingresado
	else:
		pass
		
print(f"El promedip de la clase es: {Promedio_notas}")
print(f"La nota maxima de la clase es: {Nota_max}")
	
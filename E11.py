def buscar_contacto(agenda):
	nombre = input("¿A quien desea buscar? ")
	print(" ")
	for categoria, contactos in agenda.items():
			if nombre in contactos:
				for persona, numero in contactos.items():
					if persona == nombre:
						print(f"Nombre: {nombre} Numero: {numero} Categoria: {categoria}")
						return
	print("No esta ese contacto en la agenda")
	
	return
	
def contar_contactos_por_grupo(agenda):
	for categoria, contactos in agenda.items():
		cantidad_de_contactos = len(contactos)
		print(f"En la categoria {categoria} hay {cantidad_de_contactos} contactos.")
	return
	
def mostrar_contactos(agenda):
	for categoria, contactos in agenda.items():
			for persona, numero in contactos.items():
				print(f"Nombre: {persona} Numero: {numero} Categoria: {categoria}")
	return

def agregar_contacto(agenda):
	categoria = input("¿A cual categoria pertenece la persona? ")
	nombre = input("¿Cual es el nombre de la persona? ")
	numero = input("¿Cual es su numero de telefono? ")
	agenda[categoria] = {}
	agenda[categoria][nombre] = numero
	return
	
agenda = {
    "Familia": {
        "Carlos": "0414-1234567",
        "Ana": "0412-7654321", 
    },
    "Trabajo": {
        "Luis": "0424-0001122"
    }
}

abierto = True
opcion = 0
while abierto:
	print("Agenda de contactos")
	print("1. Buscar un contacto")
	print("2. Contar contactos por grupo")
	print("3. Mostrar contactos")
	print("4. Agregar o actualizar contacto")
	print("5. Salir")
	opcion = int(input("¿Cual opcion vas a elegir? "))
	print(" ")
	if opcion == 1:
		buscar_contacto(agenda)
		print(" ")
	elif opcion == 2:
		contar_contactos_por_grupo(agenda)
		print(" ")
	elif opcion == 3:
		mostrar_contactos(agenda)
		print(" ")
	elif opcion == 4:
		agregar_contacto(agenda)
		print(" ")
	elif opcion == 5:
		abierto = False
		print("Saliendo...")
	else:
		print(" ")
		opcion = 0


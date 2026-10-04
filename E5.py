def contar_vocales(texto):
	texto_min = str.lower(texto)
	contador = 0
	for i in range(len(texto_min)):
		if texto_min[i] == "a":
			contador += 1
		elif texto_min[i] == "e":
			contador += 1
		elif texto_min[i] == "i":
			contador += 1
		elif texto_min[i] == "o":
		    contador += 1
		elif texto_min[i] =="u":
		    contador += 1
		else:
		    pass
		    	
	return contador
		 		         
print("Contador de vocales")
texto_usuario = str(input("Ingresa tu texto: "))

resultado = contar_vocales(texto_usuario);
print(resultado)

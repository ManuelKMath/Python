frase_1 = str.lower(input("Ingresa la primera frase: "))
frase_2 = str.lower(input("Ingresa la segunda frase: "))

conjunto_frase_1 = set(frase_1.split())
conjunto_frase_2 = set(frase_2.split())

print(f"Las palabras unicas que se repiten en ambas frases son: {conjunto_frase_1 & conjunto_frase_2}")
print(f"La cantidad de palabras unicas en la primera frase es: {len(conjunto_frase_1)}")








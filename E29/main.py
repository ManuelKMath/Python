
class ManejadorArchivoSeguro:
	"""Clase gestor de contexto de archivos"""
	def __init__(self, ruta: str, modo: str):
		self.ruta = ruta
		self.modo = modo
		
	def __enter__(self):
		print(f"[INICIO CONTEXTO]: Abriendo archivo en '{self.ruta}'...")
		archivo = open(self.ruta, self.modo)
		self._archivo = archivo
		return archivo

	def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
		self._archivo.close()
		print("[FIN CONTEXTO]: Archivo cerrado de forma segura.")
		if exc_type is not None:
			print(f"[LOG CONTEXTO]: Ocurrió un error dentro del bloque: {exc_val}")
		return False
		
# Flujo del programa

# Caso 1 [Funcionamiento exitoso]
with ManejadorArchivoSeguro("prueba.txt", "w") as archivo:
	archivo.write("Linea 1")
	archivo.write("Linea 2")
	archivo.write("Linea 3")
	
# Caso 2 [Error de funcionamiento]
with ManejadorArchivoSeguro("prueba.txt", "w") as archivo:
	try:
		raise ValueError
		archivo.write("Linea 4")
	except Exception:
		print("[ERROR DE ESCRITURA]")
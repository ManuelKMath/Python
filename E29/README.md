# Ejercicio de calentamiento de creación de gestores de contexto (E29)

Vas a diseñar tu propio Gestor de Contexto llamado ManejadorArchivoSeguro.

Requerimientos:
Clase ManejadorArchivoSeguro:

__init__(self, ruta: str, modo: str): Recibe la ruta del archivo y el modo ("w", "r", etc.).

__enter__(self):

Imprime "[INICIO CONTEXTO]: Abriendo archivo en '{self.ruta}'...".

Abre el archivo con open(self.ruta, self.modo) y guarda el objeto en un atributo interno self._archivo.

Retorna self._archivo (para que al hacer with ManejadorArchivoSeguro(...) as f:, f sea el objeto archivo directamente).

__exit__(self, exc_type, exc_val, exc_tb):

Cierra el archivo con self._archivo.close().

Imprime "[FIN CONTEXTO]: Archivo cerrado de forma segura.".

Si ocurrió un error (exc_type is not None), imprime "[LOG CONTEXTO]: Ocurrió un error dentro del bloque: {exc_val}".

Retorna False para propagar las excepciones.

Pruebas en main.py:

Caso 1 (Éxito): Usa el gestor para escribir tres líneas en un archivo prueba.txt.

Caso 2 (Fallo): Usa el gestor para intentar escribir, pero dentro del bloque with fuerza una excepción manual (raise ValueError("Error simulado escribiendo datos")) envuelta en un try / except externo para verificar que, a pesar del colapso, el contexto cierra el archivo y muestra la alerta.



## 📁 Estructura del Proyecto
├── main.py Código fuente donde se ejecuta el ejercicio.


DUDAS: 

Errores: 3. Detalle importante sobre la prueba en Caso 2
En tu código escribiste el try/except dentro del bloque with:

Python
# Como el try/except está DENTRO, la excepción se resuelve adentro
with ManejadorArchivoSeguro("prueba.txt", "w") as archivo:
    try:
        raise ValueError
        archivo.write("Linea 4")
    except Exception:
        print("[ERROR DE ESCRITURA]")
Como el bloque except capturó el ValueError internamente, el bloque with finalizó sin errores no controlados. Por eso __exit__ recibió exc_type = None.

Para probar que __exit__ registre el error en sus logs antes de que el cliente lo atrape, el try/except debe envolver al bloque with por fuera:

Python
# Caso 2 [Error de funcionamiento correctamente probado]
try:
    with ManejadorArchivoSeguro("prueba.txt", "w") as archivo:
        archivo.write("Linea 1\n")
        raise ValueError("Error simulado durante la escritura")
        archivo.write("Linea 2\n")  # Esto nunca se ejecuta
except ValueError as e:
    print(f"[ERROR CAPTURADO EN CLIENTE]: {e}")

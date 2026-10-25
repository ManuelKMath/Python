# Ejercicio de calentamiento de creación de decoradores (E27)

Vas a crear un decorador de Registro y Log de Auditoría llamado @auditar_ejecucion.

Requerimientos:
El Decorador (@auditar_ejecucion):

Debe imprimir en consola un mensaje inicial diciendo: "[LOG]: Ejecutando 'nombre_funcion' con args: ... y kwargs: ...".

Ejecuta la función original.

Si la función se ejecuta con éxito, imprime "[LOG]: 'nombre_funcion' finalizó correctamente. Resultado: ...".

Si la función lanza una excepción, imprime "[LOG ALERTA]: 'nombre_funcion' falló con la excepción: ..." y vuelve a lanzar la excepción (raise) para no silenciar el error.

Recuerda usar @wraps(func).

Probarlo en dos funciones:

Una función dividir(a: float, b: float) decorada con @auditar_ejecucion.

Llama a dividir(10, 2) (caso exitoso) capturando la salida.

Llama a dividir(10, 0) dentro de un bloque try/except para ver cómo el decorador registra la alerta antes de propagar la excepción.



## 📁 Estructura del Proyecto
├── main.py Código fuente donde se ejecuta el ejercicio.


DUDAS: Creo que lo único que no me queda claro es todo lo que ofrece @wraps(func), y lo que hace *args, **kwargs, se que son los parámetros posicionales y por clave, pero no sé qué es uno por clave y además quiero entender si es que wrapper toma los parámetros de dividir es cuando se pasa como parámetro por el decorador que estamos definiendo.

Errores: En esta versión escribí manualmente el texto args: a: float y b: float y capturaste únicamente ZeroDivisionError. Un decorador debe ser agnóstico: no debe saber qué tipos de datos recibe ni qué error específico lanzará la función.
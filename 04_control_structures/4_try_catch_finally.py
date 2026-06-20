# Try-Except-Finally en Python (Manejo de Excepciones)
# Version de Python: La estructura try-except-finally ha sido parte de Python desde la version 1.0 (Enero 1994).

# La estructura try-except-finally se usa para el manejo de excepciones en Python, permitiendo gestionar errores y asegurar que el codigo de limpieza se ejecute.

# Ejemplo: Manejo de excepciones con try-except-finally
try:
    result = 10 / 0  # Esto lanzara un ZeroDivisionError
except ZeroDivisionError as e:
    print('Error:', e)  # Salida (output): Error: division by zero
finally:
    print(
        "Esto se ejecutara siempre, sin importar si hay un error"
    )  # Salida (output): Esto se ejecutara siempre, sin importar si hay un error

# Capturando multiples excepciones
# Puedes manejar diferentes tipos de excepciones usando una tupla en la clausula except.
try:
    result = int("abc")  # Esto lanzara un ValueError
except (ValueError, TypeError) as e:
    print('Error:', e)  # Salida (output): Error: invalid literal for int() with base 10: 'abc'

# Usando else con try-except
# El bloque else se ejecuta si no se lanzo ninguna excepcion en el bloque try.
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error de division por cero")
else:
    print('Resultado:', result)  # Salida (output): Result: 5.0

# Usando finally para asegurar la limpieza
# El bloque finally se usa para liberar recursos o realizar acciones de limpieza.
try:
    file = open("example.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("Archivo no encontrado")
finally:
    file.close()  # Asegura que el archivo se cierre sin importar si ocurrio un error
    print("Archivo cerrado")  # Salida (output): File closed

# Nota: La estructura try-except-finally es esencial para escribir codigo Python robusto, asegurando que los recursos se gestionen y los errores se manejen de forma adecuada.

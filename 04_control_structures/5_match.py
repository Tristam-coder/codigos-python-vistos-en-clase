# Sentencia match en Python
# Version de Python: La sentencia match fue introducida en Python 3.10 (Octubre 2021).

# La sentencia match proporciona coincidencia de patrones (pattern matching),
# permitiendo un control mas legible sobre condiciones complejas.

def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "No Encontrado"
        case 500:
            return "Error Interno del Servidor"
        case _:
            return "Estado Desconocido"

# Ejemplo de uso de match
print(http_status(200))  # Salida (output): OK
print(http_status(404))  # Salida (output): No Encontrado
print(http_status(999))  # Salida (output): Estado Desconocido

# Match con patrones complejos
def describe_point(point):
    match point:
        case (0, 0):
            return "Origen"
        case (x, 0):
            return f"En el eje X en {x}"
        case (0, y):
            return f"En el eje Y en {y}"
        case (x, y) if x == y:
            return "En la linea y = x"
        case _:
            return "En otro lugar"

# Ejemplo de uso de coincidencia con tuplas
print(describe_point((0, 0)))  # Salida (output): Origen
print(describe_point((3, 0)))  # Salida (output): En el eje X en 3
print(describe_point((2, 2)))  # Salida (output): En la linea y = x

# Nota: La sentencia match permite coincidencia de patrones (pattern matching) mas expresiva,
# lo que la hace ideal para manejar condiciones complejas, como estructuras de datos o enums.

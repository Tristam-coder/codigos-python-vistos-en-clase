# Version de Python (Python Version): estos tipos existen desde Python 1.0 (January 1994),
# con algunas adiciones en versiones posteriores.

# En Python, los valores se clasifican por su tipo de dato (data type).
#
# Categorias comunes:
# - Numericos (numeric types): int, float, complex.
# - Booleano (boolean type): bool.
# - Texto (text type): str.
# - Secuencias (sequence types): list, tuple, range.
# - Mapeo (mapping type): dict.
# - Conjuntos (set types): set, frozenset.
# - Binarios (binary types): bytes, bytearray, memoryview.
# - Ausencia de valor (none/null type): NoneType, usado con None.
#
# Por que importa:
# - La categoria indica que operaciones puedes usar con cada valor.
# - Matematicamente, cada tipo define un conjunto de valores y operaciones validas.
#
# Definiciones matematicas utiles:
# - Secuencia (sequence): coleccion ordenada de elementos, con posicion o indice.
#   Ejemplo: (a0, a1, a2). El orden importa y puede haber elementos repetidos.
# - Conjunto (set): coleccion no ordenada de elementos unicos.
#   Ejemplo: {1, 2, 3}. El orden no importa y no hay elementos repetidos.
# - Vector (vector): objeto ordenado con componentes, normalmente numericas,
#   sobre el que se definen operaciones como suma y multiplicacion por escalar.
#   Se suele representar como v, vec(v), (v1, v2, ..., vn) o como vector columna.
#   En Python se puede representar con list o tuple para ejemplos simples,
#   y normalmente con numpy.ndarray cuando se hacen calculos vectoriales reales.

# Entero (integer, int): numeros completos positivos o negativos.
# Clasificacion: numerico (numeric type).
# Explicación: x pertenece a los enteros, x in Z.
x = 10  # Integer
print('x es un entero (integer):', x, '(tipo/type:', type(x), ')\n')

# Decimal (float): numeros con punto decimal.
# Clasificacion: numerico (numeric type).
# Explicación: y aproxima un numero real, y in R, con precision finita.
y = 10.5  # Float
print('y es un decimal (float):', y, '(tipo/type:', type(y), ')\n')

# Cadena (string, str): secuencia de caracteres.
# Clasificacion: texto (text type).
# Explicación: name es una cadena finita sobre un alfabeto, name in Sigma*.
name = "Alicia"  # String
print('name es una cadena (string):', name, '(tipo/type:', type(name), ')\n')

# Booleano (boolean, bool): representa valores de verdad, True o False.
# Clasificacion: booleano (boolean type).
# Explicación: is_python_fun pertenece al conjunto booleano {True, False}.
is_python_fun = True  # Boolean
print('is_python_fun es booleano (boolean):', is_python_fun, '(tipo/type:', type(is_python_fun), ')\n')

# Lista (list): secuencia ordenada de elementos.
# Clasificacion: secuencia (sequence type).
# Explicación: una lista representa una secuencia ordenada [a1, a2, ..., an].
# Si sus elementos son numeros, tambien puede representar un vector simple.
# Ejemplo matematico: [1, 2, 3] puede representar v = (1, 2, 3) en R^3.
list_sequence = [1, 2, 3]  # List
print('list_sequence es una lista (list):', list_sequence, '(tipo/type:', type(list_sequence), ')\n')

# Tupla (tuple): secuencia ordenada de elementos.
# Clasificacion: secuencia (sequence type).
# Explicación: una tupla representa una n-tupla ordenada (a1, a2, ..., an).
# Una tupla numerica tambien puede representar un vector fijo.
# Ejemplo matematico: (1, 2, 3) puede representar v = (1, 2, 3) en R^3.
tuple_sequence = (1, 2, 3)  # Tuple
print('tuple_sequence es una tupla (tuple):', tuple_sequence, '(tipo/type:', type(tuple_sequence), ')\n')

# Diccionario (dictionary, dict): coleccion de pares clave-valor (key-value pairs).
# Clasificacion: mapeo (mapping type).
# Explicación: un dict representa una funcion parcial finita f: claves -> valores.
key_value_pairs = {"clave": "valor"}  # Dictionary
print('key_value_pairs es un dict:', key_value_pairs, '(tipo/type:', type(key_value_pairs), ')\n')

# Conjunto (set): coleccion no ordenada de elementos unicos.
# Clasificacion: conjunto (set type).
# Explicación: un set representa un conjunto finito S = {x1, x2, ..., xn}, sin repetidos.
# Diferencia clave: un conjunto no tiene posiciones; por eso {1, 2, 3} no es lo mismo que un vector.
unique_items = {1, 2, 3}  # Set
print('unique_items es un conjunto (set):', unique_items, '(tipo/type:', type(unique_items), ')\n')

# Bytes (bytes): secuencia de bytes.
# Clasificacion: binario (binary type).
# Explicación: bytes es una secuencia (b1, ..., bn) donde cada bi esta en {0, ..., 255}.
byte_data = b"hola"  # Bytes
print('byte_data es bytes:', byte_data, '(tipo/type:', type(byte_data), ')\n')

# Bytearray (bytearray): secuencia de bytes.
# Clasificacion: binario (binary type).
# Explicación: bytearray es una secuencia de valores bi en {0, ..., 255}.
byte_array_data = bytearray(b"hola")  # Bytearray
print('byte_array_data es bytearray:', byte_array_data, '(tipo/type:', type(byte_array_data), ')\n')

# NoneType (None): representa la ausencia de valor o un valor nulo (null value).
# Clasificacion: ausencia de valor (none/null type).
# Explicación: None puede verse como el unico elemento del conjunto singleton {None}.
nothing = None  # NoneType
print('nothing es NoneType:', nothing, '(tipo/type:', type(nothing), ')\n')

# Rango (range): secuencia de numeros usada comunmente en bucles (loops).
# Clasificacion: secuencia (sequence type).
# Explicación: range(start, stop, step) representa a_n = start + n*step, con a_n < stop.
# Es una secuencia porque tiene orden e indices; no es un conjunto porque el orden importa.
num_range = range(0, 10)  # Range
print('num_range es range:', list(num_range), '(tipo/type:', type(num_range), ')\n')

# Frozenset (frozenset): conjunto de elementos unicos.
# Clasificacion: conjunto (set type).
# Explicación: frozenset representa un conjunto finito fijo S = {x1, ..., xn}.
# Es conjunto porque no tiene orden ni elementos repetidos.
frozen_set = frozenset([1, 2, 3])  # Frozenset
print('frozen_set es frozenset:', frozen_set, '(tipo/type:', type(frozen_set), ')\n')

# Complejo (complex): numero con parte real e imaginaria.
# Clasificacion: numerico (numeric type).
# Explicación: z pertenece a los complejos, z = a + bi, con i^2 = -1.
z = 3 + 4j  # Complex number
print('z es un numero complejo (complex):', z, '(tipo/type:', type(z), ')\n')

# Memoryview (memoryview): permite ver memoria de objetos binarios sin copiar.
# Clasificacion: binario (binary type); puede ser de solo lectura o escribible segun el objeto base.
# Explicación: memoryview es una vista sobre una secuencia de bytes, sin duplicar la secuencia.
memory_view = memoryview(b"hola")  # Memoryview
print('memory_view es memoryview:', memory_view, '(tipo/type:', type(memory_view), ')\n')

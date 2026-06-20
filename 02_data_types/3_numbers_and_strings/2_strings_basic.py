# Operaciones basicas con cadenas (strings) en Python.
# Version de Python (Python Version): las cadenas existen desde Python 1.0
# y evolucionaron con mejoras como soporte Unicode en Python 3.0 (December 2008).

# Las cadenas (strings) son secuencias de caracteres usadas para guardar texto.
# Explicación: un string es una secuencia finita s = (c0, c1, ..., c(n-1)).

# Concatenacion (concatenation).
# Explicación: si s = "Hola" y t = "Mundo", entonces s + " " + t concatena secuencias.
str1 = "Hola"
str2 = "Mundo"
combined_str = str1 + " " + str2  # Combina strings usando el operador '+'.
print(combined_str)  # Salida (output): Hola Mundo

# Repeticion (repetition).
# Explicación: s * 3 = s + s + s.
repeat_str = "Python! " * 3  # Repite strings usando el operador '*'.
print(repeat_str)  # Salida: Python! Python! Python!

# Acceso a caracteres (accessing characters).
# Explicación: str1[0] devuelve el primer elemento de la secuencia, c0.
first_char = str1[0]  # Los strings se indexan desde 0.
print('Primer caracter de str1:', first_char)  # Salida: H

# Rebanado (slicing).
# Explicación: str1[1:4] devuelve la subsecuencia con indices 1 <= i < 4.
slice_str = str1[1:4]  # Extrae una subcadena (substring) del string.
print('Subcadena con slicing:', slice_str)  # Salida: ola

# Nota: los strings de Python son inmutables (immutable):
# no se pueden cambiar despues de ser creados.

# Metodos comunes de cadenas (string methods) en Python.
# Version de Python (Python Version): los metodos de string han mejorado con el tiempo;
# muchos existen desde Python 1.0.

# Python ofrece muchos metodos para manipular y analizar cadenas (strings).
# Explicación: los metodos de string son funciones que transforman o consultan secuencias.

text = "Hola, Python!"

# Convertir a mayusculas (uppercase).
# Explicación: upper aplica una funcion caracter a caracter: c -> MAYUSCULA(c).
uppercase_text = text.upper()
print('Mayusculas (uppercase):', uppercase_text)  # Salida (output): HOLA, PYTHON!

# Convertir a minusculas (lowercase).
# Explicación: lower aplica una funcion caracter a caracter: c -> minuscula(c).
lowercase_text = text.lower()
print('Minusculas (lowercase):', lowercase_text)  # Salida: hola, python!

# Dividir en una lista de palabras (split).
# Explicación: split separa una secuencia en subsecuencias usando un separador.
words = text.split()  # Por defecto, split separa por espacios en blanco (whitespace).
print('Palabras (words):', words)  # Salida: ['Hola,', 'Python!']

# Buscar una subcadena (substring).
# Explicación: find devuelve el menor indice i donde aparece la subcadena, o -1 si no aparece.
position = text.find("Python")
print("Posicion de 'Python':", position)  # Salida: 6

# Reemplazar una subcadena (replace).
# Explicación: replace transforma una secuencia sustituyendo ocurrencias de una subsecuencia por otra.
new_text = text.replace("Python", "Mundo")
print('Texto reemplazado (replaced text):', new_text)  # Salida: Hola, Mundo!

# Nota: Python tiene muchos string methods para manipulacion completa de texto.

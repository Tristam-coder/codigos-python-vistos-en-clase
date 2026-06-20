# Version de Python (Python Version): introducido en Python 1.0 (January 1994).

# La funcion print() se usa para enviar datos a la consola (console output).
# Puede recibir varios argumentos (arguments), separados por espacios en la salida.
# Explicación: print puede verse como una funcion de salida f(valores) -> texto en consola.

# En Python, las cadenas (strings) pueden usar comillas simples ('') o dobles ("").
# print() agrega automaticamente un salto de linea (newline) al final de cada salida.
# Explicación: una cadena es una secuencia finita de caracteres: s = (c1, c2, ..., cn).
print("Hola Mundo")  # Salida (output): Hola Mundo

# Puedes imprimir varios argumentos separados por comas.
# Explicación: print(a, b, c) concatena representaciones: str(a) + " " + str(b) + " " + str(c).
print("Python", "es", "divertido")  # Salida: Python es divertido

# El argumento sep define el texto que separa los objetos.
print("Python", "es", "divertido", sep="-")  # Salida: Python-es-divertido

# Expresiones dentro de print()
# Explicación: 2 + 2 representa la suma en los enteros: 2 + 2 = 4.
print("La suma de 2 + 2 es:", 2 + 2, "unidades")  # Salida: La suma de 2 + 2 es: 4

# infinity_operations.py

# Valores numericos especiales (special numeric values) en Python: infinito (Infinity).
# Explicación: se trabaja con reales extendidos R_ext = R union {-inf, +inf}.

import math

import numpy as np

# Obtener infinito (Infinity, inf) directamente.

# Usando el constructor (constructor) float.
# Explicación: +inf representa un valor mayor que cualquier numero real finito.
infinity = float("inf")
print("Infinito positivo usando float('inf'):", infinity)  # Salida (output): inf
print()

# Usando la constante (constant) math.inf (Python 3.5+).
# Explicación: math.inf tambien representa +inf.
infinity_math = math.inf
print('Infinito positivo usando math.inf:', infinity_math)  # Salida: inf
print()

# Usando la constante de infinito de NumPy.
# Explicación: np.inf representa +inf en operaciones numericas de NumPy.
infinity_np = np.inf
print('Infinito positivo usando np.inf:', infinity_np)  # Salida: inf
print()

# Obtener infinito negativo (negative infinity) directamente.

# Usando el constructor float.
# Explicación: -inf representa un valor menor que cualquier numero real finito.
neg_infinity = float("-inf")
print("Infinito negativo usando float('-inf'):", neg_infinity)  # Salida: -inf
print()

# Usando la constante math.inf negada.
# Explicación: -(+inf) = -inf.
neg_infinity_math = -math.inf
print('Infinito negativo usando -math.inf:', neg_infinity_math)  # Salida: -inf
print()

# Usando la constante de infinito negativo de NumPy.
# Explicación: -np.inf representa -inf.
neg_infinity_np = -np.inf
print('Infinito negativo usando -np.inf:', neg_infinity_np)  # Salida: -inf
print()

# Obtener infinito (inf) mediante operaciones.

# Division por cero (numero positivo).
# Explicación: el limite de 1/x cuando x -> 0+ es +inf.
try:
    infinity = 1.0 / 0.0  # Esto produce un error en circunstancias normales.
except ZeroDivisionError:
    infinity = float("inf")
print('Infinito positivo por division:', infinity)  # Salida: inf
print()

# Infinito negativo al dividir un numero negativo entre cero.
# Explicación: el limite de -1/x cuando x -> 0+ es -inf.
try:
    neg_infinity = -1.0 / 0.0  # Esto produce un error en circunstancias normales.
except ZeroDivisionError:
    neg_infinity = float("-inf")
print('Infinito negativo por division:', neg_infinity)  # Salida: -inf
print()

# Exponenciacion (exponentiation) o multiplicacion con un numero muy grande.
# Explicación: si un resultado excede el maximo float, se aproxima como +inf.
large_number = 1e308
infinity_exp = large_number * large_number  # Esto resulta en infinito.
print('Infinito por multiplicacion de numero grande:', infinity_exp)  # Salida: inf
print()

# Operaciones con infinito (Infinity).
# Explicación: para c finito positivo, +inf + c = +inf, +inf * c = +inf.
print('Infinito + 1:', infinity + 1)  # Salida: inf
print()

print('Infinito - 1000:', infinity - 1000)  # Salida: inf
print()

print('Infinito * 2:', infinity * 2)  # Salida: inf
print()

print('Infinito / 2:', infinity / 2)  # Salida: inf
print()

print('Infinito + Infinito:', infinity + infinity)  # Salida: inf
print()

# Explicación: +inf - +inf es una forma indeterminada, no un numero real definido.
print('Infinito - Infinito:', infinity - infinity)  # Salida: nan (forma indeterminada / indeterminate form)
print()

# Explicación: +inf * 0 tambien es una forma indeterminada.
print('Infinito * 0:', infinity * 0)  # Salida: nan (forma indeterminada)
print()

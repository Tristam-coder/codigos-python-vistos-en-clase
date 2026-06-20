# nan_operations.py

# Valores numericos especiales (special numeric values) en Python: NaN (Not a Number).
# Explicación: NaN representa resultados indefinidos o no representables como numero real.

import math

import numpy as np

# Obtener NaN (Not a Number) directamente.

# Usando el constructor (constructor) float.
# Explicación: NaN no pertenece a R; se usa como marcador de operacion indefinida.
nan = float("nan")
print("NaN usando float('nan'):", nan)  # Salida (output): nan
print()

# Usando la constante (constant) math.nan (Python 3.5+).
# Explicación: math.nan representa el mismo concepto de "not a number".
nan_math = math.nan
print('NaN usando math.nan:', nan_math)  # Salida: nan
print()

# Usando la constante NaN de NumPy.
# Explicación: np.nan propaga valores indefinidos en arreglos y calculos numericos.
nan_np = np.nan
print('NaN usando np.nan:', nan_np)  # Salida: nan
print()

# Obtener NaN mediante operaciones.

# Raiz cuadrada de un numero negativo (normalmente lanza ValueError).
# Explicación: sqrt(-1) no pertenece a R; en los complejos seria i.
try:
    nan_sqrt = math.sqrt(
        -1.0
    )  # Normalmente lanzaria ValueError; conceptualmente se representa como NaN.
except ValueError:
    nan_sqrt = float("nan")
print('NaN por raiz cuadrada negativa:', nan_sqrt)  # Salida: nan
print()

# 0 dividido entre 0 (normalmente lanza ZeroDivisionError).
# Explicación: 0/0 es indeterminado porque cualquier x cumple 0*x = 0.
try:
    nan_div = 0.0 / 0.0  # Esto produce un error en circunstancias normales.
except ZeroDivisionError:
    nan_div = float("nan")
print('NaN por division 0/0:', nan_div)  # Salida: nan
print()

# Infinito menos infinito.
# Explicación: +inf - +inf es una forma indeterminada.
infinity = float("inf")
nan_subtract = infinity - infinity
print('NaN al restar infinito de infinito:', nan_subtract)  # Salida: nan
print()

# 0 multiplicado por infinito.
# Explicación: 0 * +inf es una forma indeterminada.
nan_multiply = 0.0 * infinity
print('NaN al multiplicar 0 por infinito:', nan_multiply)  # Salida: nan
print()

# Operaciones con NaN.
# Explicación: si una operacion incluye NaN, el resultado suele propagarse como NaN.
print('NaN + 1:', nan + 1)  # Salida: nan
print()

print('NaN - 1000:', nan - 1000)  # Salida: nan
print()

print('NaN * 2:', nan * 2)  # Salida: nan
print()

print('NaN / 2:', nan / 2)  # Salida: nan
print()

print('NaN + Infinito:', nan + infinity)  # Salida: nan
print()

print('NaN - Infinito:', nan - infinity)  # Salida: nan
print()

print('NaN * Infinito:', nan * infinity)  # Salida: nan
print()

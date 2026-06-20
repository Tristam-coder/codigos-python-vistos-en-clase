# Operadores de asignacion (assignment operators) en Python.
# Version de Python (Python Version): existen desde Python 1.0 (January 1994).

# Los operadores de asignacion guardan valores en variables (variables);
# a menudo combinan una operacion con la asignacion.
# Explicación: una variable es un nombre asociado a un valor; la asignacion actualiza esa asociacion.

# Asignacion simple (simple assignment, =).
# Explicación: x <- 10.
x = 10
print('x = 10:', x)  # Salida (output): x = 10

# Sumar y asignar (add and assign, +=).
# Explicación: x <- x + 5; si x = 10, entonces x = 15.
x += 5  # Equivalente a: x = x + 5
print('x += 5:', x)  # Salida: x += 5: 15

# Restar y asignar (subtract and assign, -=).
# Explicación: x <- x - 3; si x = 15, entonces x = 12.
x -= 3  # Equivalente a: x = x - 3
print('x -= 3:', x)  # Salida: x -= 3: 12

# Multiplicar y asignar (multiply and assign, *=).
# Explicación: x <- x * 2; si x = 12, entonces x = 24.
x *= 2  # Equivalente a: x = x * 2
print('x *= 2:', x)  # Salida: x *= 2: 24

# Dividir y asignar (divide and assign, /=).
# Explicación: x <- x / 4; si x = 24, entonces x = 6.0.
x /= 4  # Equivalente a: x = x / 4
print('x /= 4:', x)  # Salida: x /= 4: 6.0

# Division entera y asignacion (floor divide and assign, //=).
# Explicación: x <- floor(x / 2); si x = 6.0, entonces x = 3.0.
x //= 2  # Equivalente a: x = x // 2
print('x //= 2:', x)  # Salida: x //= 2: 3.0

# Modulo y asignacion (modulus and assign, %=).
# Explicación: x <- x mod 2; si x = 3.0, entonces x = 1.0.
x %= 2  # Equivalente a: x = x % 2
print('x %= 2:', x)  # Salida: x %= 2: 1.0

# Exponenciar y asignar (exponentiate and assign, **=).
# Explicación: x <- x^3; si x = 1.0, entonces x = 1.0.
x **= 3  # Equivalente a: x = x ** 3
print('x **= 3:', x)  # Salida: x **= 3: 1.0

# Nota: estos operadores son atajos (shorthand) para operar y guardar el resultado en la misma variable.

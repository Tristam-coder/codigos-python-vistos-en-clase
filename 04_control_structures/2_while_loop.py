# While Loops en Python
# Version de Python: El bucle (loop) while ha sido parte de Python desde la version 1.0 (enero de 1994).

# El bucle (loop) while ejecuta repetidamente un bloque de codigo mientras la condicion (condition) sea True.
# Es util cuando el numero de iteraciones no se conoce de antemano.

# Ejemplo: Bucle (loop) while basico
count = 0

while count < 5:
    print('Contador:', count)
    count += 1  # Incrementar el contador

# Ejemplo: Uso del bucle (loop) while para sumar numeros hasta que se cumpla una condicion (condition)
total = 0
number = 1

while number <= 10:
    total += number
    number += 1

print('Suma total de 1 a 10 es:', total)  # Salida (output): Suma total de 1 a 10 es: 55

# Bucle (loop) infinito (usar con precaucion)
# Un bucle (loop) infinito se ejecuta para siempre a menos que se detenga externamente o se rompa desde dentro.
# Descomenta las lineas de abajo para crear un bucle (loop) infinito
# while True:
#     print("Esto se ejecutara para siempre")

# Uso del bucle (loop) while con una condicion (condition) de ruptura (break)
n = 10
while n > 0:
    print('Cuenta regresiva:', n)
    n -= 1
    if n == 5:
        print("Rompiendo el bucle (loop)")
        break  # Salir del bucle (loop) cuando n sea 5

# Nota: Los bucles (loops) while proporcionan flexibilidad para condiciones (conditions) que dependen de valores dinamicos, pero se debe tener cuidado para evitar bucles (loops) infinitos.

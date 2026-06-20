# Las funciones impuras pueden producir diferentes resultados incluso con los mismos inputs
# y pueden modificar el estado externo o producir efectos secundarios (side effects).

# Ejemplo Clasico de Random
# El uso de generacion de numeros aleatorios es un ejemplo comun de una funcion impura,
# porque produce diferentes salidas (outputs) para el mismo input.

import random


def generate_random_number():
    # Esta funcion genera un numero aleatorio entre 1 y 10.
    # La salida (output) varia cada vez que se llama, lo que la convierte en una funcion impura.
    return random.randint(1, 10)


# Llama a la funcion multiples veces
random_result_1 = generate_random_number()
random_result_2 = generate_random_number()

# Las salidas (outputs) probablemente seran diferentes, lo que demuestra la impureza de la
# funcion.
print('Numero Aleatorio 1:', random_result_1)
print('Numero Aleatorio 2:', random_result_2)

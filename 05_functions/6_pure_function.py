# Funciones Puras e Impuras en Python
# Una funcion pura es aquella en la que la salida (output) depende solo de sus entradas
# y no tiene efectos secundarios. Las funciones impuras, sin embargo, pueden modificar
# estados externos o producir efectos secundarios.


##########################################################


# Ejemplo de Funcion Pura
# Las funciones puras siempre devuelven el mismo resultado para la misma entrada (input)
# y no modifican ningun estado externo.

def pure_add(a, b):
    # Esta funcion suma dos numeros y devuelve el resultado.
    # No modifica ningun estado externo, lo que la convierte en una funcion pura.
    # Punto clave: Para los mismos valores de entrada (input), la salida (output) siempre sera la misma.
    return a + b


# Llamar a la funcion
pure_result_1 = pure_add(5, 3)  # Salida: 8
pure_result_2 = pure_add(5, 3)  # Salida: 8

# Como la funcion es pura, pure_result_1 y pure_result_2 siempre seran iguales.
print('Resultado de la Funcion Pura 1:', pure_result_1)  # Salida: Resultado de la Funcion Pura 1: 8
print('Resultado de la Funcion Pura 2:', pure_result_2)  # Salida: Resultado de la Funcion Pura 2: 8

# Ventajas de las Funciones Puras:
# - Predecibilidad: Siempre producen la misma salida (output) para la misma entrada (input), lo que las hace confiables y faciles de entender.
# - Sin Efectos Secundarios: No alteran el estado externo, lo que las hace mas seguras y faciles de probar.
# - Mas Faciles de Paralelizar: Se pueden paralelizar u optimizar mas facilmente debido a su falta de efectos secundarios.

# Desventajas de las Funciones Puras:
# - Uso Limitado: No pueden realizar acciones que requieran efectos secundarios (por ejemplo, registro, actualizaciones de base de datos).
# - Pueden Requerir Codigo Adicional: Evitar los efectos secundarios puede llevar a un codigo mas complejo.

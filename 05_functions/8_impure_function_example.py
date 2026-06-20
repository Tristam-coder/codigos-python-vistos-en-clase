# Las funciones impuras pueden producir diferentes resultados incluso con los mismos inputs (entradas)
# y pueden modificar el estado externo o producir efectos secundarios (side effects).

# Ejemplo de Funcion Impura

def impure_add_and_log(a, b, log):
    # Esta funcion suma dos numeros y agrega el resultado a una lista de log.
    # Modificar la lista de log es un efecto secundario, lo que hace que esta funcion sea impura.
    # Punto clave: La funcion puede producir diferentes resultados incluso si los inputs son los mismos,
    # porque depende y modifica estado externo.
    result = a + b
    log.append(result)  # Efecto secundario: modificar la lista 'log' externa
    return result


# Llamar a la funcion
log_list = []  # Estado externo que sera modificado por la funcion
impure_result_1 = impure_add_and_log(5, 3, log_list)  # Salida (output): 8, log_list: [8]
impure_result_2 = impure_add_and_log(5, 3, log_list)  # Salida (output): 8, log_list: [8, 8]

# La log_list se modifica como efecto secundario, haciendo que la funcion sea impura.
print('Funcion Impura Resultado 1:', impure_result_1)  # Salida (output): Funcion Impura Resultado 1: 8
print('Funcion Impura Resultado 2:', impure_result_2)  # Salida (output): Funcion Impura Resultado 2: 8
print('Lista de Log:', log_list)  # Salida (output): Lista de Log: [8, 8]


# Ventajas de las Funciones Impuras:
# - Flexibilidad: Pueden modificar estado externo o interactuar con sistemas externos.
# - Directas y Practicas: Utiles para tareas que requieren efectos secundarios (por ejemplo, logging, actualizaciones de base de datos, generacion de numeros aleatorios).

# Desventajas de las Funciones Impuras:
# - Impredecibilidad: Pueden ser mas difficiles de probar y depurar debido a su dependencia del estado externo y los efectos secundarios.
# - Potencial de Errores: Los efectos secundarios pueden provocar cambios no deseados y errores sutiles, especialmente en sistemas complejos.


##########################################################


# Pasando Estado Externo a Funciones
# Para evitar variables globales, el estado externo se puede pasar como argumento.
# Aunque esto reduce la dependencia del estado global, la funcion aun puede ser impura
# si modifica el estado externo.

# Un mejor enfoque es devolver el estado modificado en lugar de modificarlo directamente:
def improved_impure_add_and_log(a, b, log):
    # Esta funcion suma dos numeros y devuelve una nueva lista de log con el resultado agregado.
    # Este enfoque evita modificar directamente el estado externo, lo que lo hace ligeramente mejor,
    # pero aun se considera impura.
    result = a + b
    new_log = log + [result]  # Crea una nueva lista en lugar de modificar la original
    return result, new_log


# Llamar a la funcion
log_list = []  # Estado externo
impure_result_3, updated_log = improved_impure_add_and_log(5, 3, log_list)

# La log_list original permanece sin cambios, pero la funcion aun es impura ya que depende del estado externo.
print('Funcion Impura Resultado 3:', impure_result_3)  # Salida (output): Funcion Impura Resultado 3: 8
print('Lista de Log Original:', log_list)  # Salida (output): Lista de Log Original: []
print('Lista de Log Actualizada:', updated_log)  # Salida (output): Lista de Log Actualizada: [8]

# Conclusion:
# - Las funciones puras son generalmente preferidas por su predecibilidad, facilidad de prueba y ausencia de efectos secundarios.
# - Las funciones impuras son necesarias para tareas que requieren interaccion con sistemas externos o modificacion del estado externo.
# - En la practica, a menudo se utiliza una mezcla de funciones puras e impuras, donde las funciones puras manejan la logica central y las funciones impuras gestionan los efectos secundarios.

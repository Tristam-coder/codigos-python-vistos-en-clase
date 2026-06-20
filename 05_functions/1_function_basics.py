# Python Version: Las funciones han sido una parte fundamental de Python desde
# la version 1.0 (enero de 1994).

# Funcion Basica en Python
# Las funciones son bloques de codigo reutilizables disenados para realizar una tarea especifica.
# Ayudan a organizar el codigo, haciendolo mas modular, mantenible y reutilizable.


# Definiendo una funcion basica
def greet():
    # Esta funcion simplemente imprime un mensaje de saludo.
    print("Hola Mundo")


# Llamando a la funcion
greet()  # Salida (output): Hello, World!


##########################################################


# Funciones con Parametros
# Los parametros permiten pasar datos a una funcion
def greet_user(name):
    # El parametro 'name' se usa para personalizar el saludo.
    print('Hola', name)


greet_user("Marcos")  # Salida (output): Hello, Marcos!


##########################################################


# Funciones con Valores de Retorno
# Las funciones pueden devolver un valor usando la sentencia 'return'.
def add(a, b):
    # Esta funcion devuelve la suma de dos numeros.
    return a + b


result = add(5, 3)
print('Sum:', result)  # Salida (output): Sum: 8


##########################################################


# Valores por Defecto de los Parametros
# Las funciones pueden tener valores por defecto en sus parametros, los cuales
# se usan si no se proporciona un argumento.
def greet_user_default(name="Guest"):
    # Si no se proporciona un nombre, 'Guest' se usara como valor por defecto.
    print('Hola', name)


greet_user_default()  # Salida (output): Hola Guest
greet_user_default("Bob")  # Salida (output): Hola Bob


##########################################################


# Argumentos Posicionales y Parametro por Defecto
# Cuando se usan argumentos posicionales y parametros por defecto al mismo
# tiempo, los parametros por defecto deben colocarse despues de los argumentos
# posicionales.
def greet_user(a, b, name="Guest"):
    print('Hola,', name)
    print('Suma:', a + b)


# Llamar a la funcion
greet_user(2, 3)  # Salida (output): Hola Marcos Sum: 5
greet_user(2, 3, "Marcos")  # Salida (output): Hola Marcos Sum: 5

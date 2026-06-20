# 1. Las funciones (functions) en Python pueden ser tratadas como valores y asignadas a variables.
def greet(name):
    return f"Hola, {name}!"


# Asignando la funcion greet a la variable say_hello
say_hello = greet

# Ahora say_hello puede ser usada como una funcion.
print(say_hello("Marcos"))  # Salida (output): Hola, Marcos


###################################################


# 2. Las funciones tambien pueden ser pasadas como argumentos a otras funciones.
def welcome_message(func, name):
    return func(name)


# Pasando la funcion greet como argumento a welcome_message
print(welcome_message(greet, "Bob"))  # Salida (output): Hola, Bob!


###################################################

# 3. Las funciones pueden ser retornadas desde otras funciones.
def get_greeting_func():
    return greet


# Obteniendo una funcion como valor de retorno y llamandola
greet_func = get_greeting_func()
print(greet_func("Charlie"))  # Salida (output): Hola, Charlie!

# En Python, las funciones son ciudadanas de primera clase (first-class citizens).
# Esto significa que las funciones pueden ser asignadas a variables, pasadas como
# argumentos a otras funciones, y retornadas desde funciones al igual que cualquier
# otro objeto. Esto permite patrones de programacion flexibles y dinamicos, como
# funciones de orden superior (higher-order functions) y decoradores de funciones
# (function decorators).

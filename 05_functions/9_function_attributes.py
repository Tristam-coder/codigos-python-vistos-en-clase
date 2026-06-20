# En Python, las funciones (functions) pueden tener atributos al igual que los objetos. Estos atributos se almacenan en el __dict__ de la funcion (function).
# Esto permite almacenar informacion adicional relacionada con una funcion (function) mas alla de su logica de codigo.

def my_function():
    print("Esta es una funcion (function) simple.")

# Asignar un atributo a la funcion (function).
my_function.description = "Esta funcion (function) imprime un mensaje."

# Acceder al atributo de la funcion (function).
print(my_function.description)  # Salida (output): 'Esta funcion (function) imprime un mensaje.'

# Puedes inspeccionar todos los atributos de la funcion (function) usando su __dict__.
print(my_function.__dict__)  # Salida (output) del diccionario de atributos de la funcion (function).

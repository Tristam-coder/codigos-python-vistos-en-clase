# Version de Python (Python Version): input() fue introducido en Python 2.0 (October 2000).

# La funcion input() permite recibir entrada (input) del usuario desde la consola.
# La ejecucion se pausa hasta que el usuario escribe algo y presiona Enter.
# Explicación: input puede verse como una funcion f(prompt) -> respuesta, donde la respuesta es un string.

# Usamos input() para capturar el nombre del usuario (user).
# Explicación: name pertenece al conjunto de cadenas posibles, name in Sigma*.
name = input(
    "Ingresa tu nombre: "
)  # La entrada se guarda en la variable (variable) 'name'.

# Una f-string (formatted string literal) es una forma moderna de dar formato a cadenas.
# Permite insertar expresiones dentro de una cadena (string) usando llaves {}.
# Explicación: el formato aplica una funcion g(name) = "Hola, " + name
print('Hola,', name)  # Salida (output): Hola, <name>

# Capturamos otra entrada del usuario.
# Aqui pedimos que ingrese su edad.
# Nota: input() devuelve una cadena (string). Si necesitas un numero, debes convertirlo.
# Explicación: age primero es texto; si se convierte, podria representar un numero natural n >= 0.
age = input("Ingresa tu edad: ")

# La f-string se usa otra vez para incluir el valor de 'age' en la salida.
# Explicación: h(age) = "Tienes " + age + " años.".
print('Tienes', age, 'años.')  # Salida: Tienes <age> años.

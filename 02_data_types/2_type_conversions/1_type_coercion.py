# Conversion implicita de tipos en Python (type coercion).
# Version de Python (Python Version): existe desde los inicios de Python.

# La conversion implicita (implicit type conversion) ocurre cuando Python convierte automaticamente
# un tipo de dato (data type) a otro durante una operacion.
# Este concepto aparece en muchas operaciones comunes.
# Explicación: una conversion puede verse como una funcion c: TipoA -> TipoB.

# Conversion de entero (integer) a float, de forma implicita.
# Explicación: 10 in Z se convierte a 10.0 in R aproximado; 10 / 2 = 5.0.
num = 10
result = num / 2  # El entero 10 se convierte implicitamente a float durante la division.
print('Resultado de la division:', result, '(tipo/type:', type(result), ')')
# Salida (output): 5.0 (type: <class 'float'>)

# Ejemplo de conversion explicita (explicit conversion).
# Explicación: str(age) aplica una funcion f: Z -> Sigma*, entonces 30 -> "30".
age = 30
age_str = "Mi edad es " + str(age)  # El entero 30 se convierte explicitamente a string.
print(age_str)  # Salida: Mi edad es 30

# Conversion de entero (integer) a booleano (boolean), de forma implicita.
# Explicación: bool(0) = False; para muchos valores numericos distintos de 0, bool(n) = True.
count = 0
# El entero 0 se convierte implicitamente a booleano (False).
if count:  
    print("El contador no es cero.")
else:
    print("El contador es cero.")  # Salida: El contador es cero.

# Conversion de booleano (boolean) a entero (integer), de forma implicita.
# Explicación: True se representa como 1 y False como 0; por eso True + 1 = 2.
is_valid = True
number = is_valid + 1  # True se convierte implicitamente a 1.
print('Numero:', number, '(tipo/type:', type(number), ')')
# Salida: Numero: 2 (type: <class 'int'>)


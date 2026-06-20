# Conversion explicita de tipos en Python (explicit type conversion).

# La conversion explicita cambia deliberadamente un tipo de dato (data type) a otro,
# normalmente con funciones incorporadas (built-in functions) como int(), str() o float().
# A diferencia de una conversion implicita, aqui el desarrollador especifica el tipo deseado.
# Explicación: cada conversion es una funcion parcial o total entre conjuntos de valores.

# Conversion de entero (integer) a cadena (string), explicita.
# Explicación: str: Z -> Sigma*, entonces str(30) = "30".
age = 30
age_str = str(age)  # Conversion explicita de integer a string.
print(age_str)  # Salida (output): "30" (type: <class 'str'>)

# Conversion de float a entero (integer), explicita.
# Explicación: int(9.99) = 9 porque Python trunca hacia 0.
value = 9.99
int_value = int(value)  # Conversion explicita de float a integer.
print('Valor entero:', int_value, '(tipo/type:', type(int_value), ')')  # Salida: Valor entero: 9 (type: <class 'int'>)

# Conversion de cadena (string) a entero (integer), explicita.
# Explicación: int("100") interpreta los digitos decimales y produce 100 in Z.
num_str = "100"
num_int = int(num_str)  # Conversion explicita de string a integer.
print('Valor entero:', num_int, '(tipo/type:', type(num_int), ')')  # Salida: Valor entero: 100 (type: <class 'int'>)

# Conversion de float a cadena (string), explicita.
# Explicación: str(3.14159) representa el numero como una cadena de simbolos.
pi = 3.14159
pi_str = str(pi)  # Conversion explicita de float a string.
print('Valor string:', pi_str, '(tipo/type:', type(pi_str), ')')  # Salida: Valor string: "3.14159" (type: <class 'str'>)

# Conversion de booleano (boolean) a entero (integer), explicita.
# Explicación: int(True) = 1 e int(False) = 0.
is_valid = True
num = int(is_valid)  # Conversion explicita de boolean a integer.
print('Valor entero:', num, '(tipo/type:', type(num), ')')  # Salida: Valor entero: 1 (type: <class 'int'>)

# Conversion de lista (list) a tupla (tuple), explicita.
# Explicación: [1, 2, 3] y (1, 2, 3) contienen la misma secuencia ordenada de elementos.
list_items = [1, 2, 3]
tuple_items = tuple(list_items)  # Conversion explicita de list a tuple.
print('Tupla (tuple):', tuple_items, '(tipo/type:', type(tuple_items), ')')  # Salida: Tupla (tuple): (1, 2, 3) (type: <class 'tuple'>)

# Conversion de cadena (string) a float, explicita.
# Explicación: float("123.45") interpreta la cadena como un numero real aproximado 123.45.
float_str = "123.45"
float_num = float(float_str)  # Conversion explicita de string a float.
print('Valor float:', float_num, '(tipo/type:', type(float_num), ')')  # Salida: Valor float: 123.45 (type: <class 'float'>)

# Conversion de tupla (tuple) a lista (list), explicita.
# Explicación: (4, 5, 6) y [4, 5, 6] representan la misma secuencia, con distinta mutabilidad.
tuple_items = (4, 5, 6)
list_items = list(tuple_items)  # Conversion explicita de tuple a list.
print('Lista (list):', list_items, '(tipo/type:', type(list_items), ')')  # Salida: Lista (list): [4, 5, 6] (type: <class 'list'>)

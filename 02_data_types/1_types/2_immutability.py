# Inmutabilidad (immutability) en Python.
# Version de Python (Python Version): la inmutabilidad de ciertos tipos existe desde versiones tempranas.

# En Python, algunos tipos de datos son inmutables (immutable):
# sus valores no se pueden cambiar despues de ser creados.
# Los tipos inmutables mas comunes son enteros, floats, strings y tuplas.
# Explicación: inmutable significa que un valor v permanece fijo; una "modificacion" crea otro valor v'.

# Ejemplo con entero (integer)
# Explicación: a0 = 10.
a = 10
print('Valor original de a:', a)

# Intentar modificar un entero crea realmente un nuevo objeto (object).
# Explicación: a1 = a0 + 5 = 15; no cambia 10, se reasigna el nombre a.
a = a + 5
print('Nuevo valor de a:', a)
# Aqui se crea un nuevo objeto entero y 'a' se reasigna (reassigned) a ese objeto.

# Ejemplo con cadena (string)
# Explicación: greeting es una secuencia s = ("H", "o", "l", "a").
greeting = "Hola"
print('Saludo original:', greeting)

# Las cadenas son inmutables, asi que cualquier cambio crea una nueva cadena.
# Explicación: s2 = s1 + t, donde + es concatenacion de secuencias.
greeting += ", Mundo!"
print('Saludo modificado:', greeting)

# Ejemplo con tupla (tuple)
# Explicación: my_tuple = (1, 2, 3) es una 3-tupla fija.
my_tuple = (1, 2, 3)
print('Tupla original:', my_tuple)

# Intentar modificar una tupla produce un error.
# Si descomentas la linea siguiente, se lanzara un TypeError.
# Explicación: la operacion my_tuple[0] <- 4 no esta definida para tuplas inmutables.
# my_tuple[0] = 4  # TypeError: 'tuple' object does not support item assignment

# Nota: la inmutabilidad ayuda a proteger la integridad de los datos y facilita razonar sobre el codigo.

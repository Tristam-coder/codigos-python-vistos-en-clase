# Sentencias If-Else en Python
# Version de Python: La estructura de control if-else ha sido parte de Python desde la version 1.0 (enero de 1994).

# La sentencia if-else te permite ejecutar cierto codigo basado en una condicion.
# Es la forma mas basica de flujo de control y es fundamental para la toma de decisiones en cualquier programa.

x = 10

# Estructura basica de if-else
# El bloque if se ejecuta si la condicion es True (verdadero).
# Si la condicion es False (falso), el bloque else (si esta presente) se ejecutara.
if x > 5:
    print("x es mayor que 5")
else:
    print("x no es mayor que 5")  # Este bloque no se ejecutara ya que x > 5 es True (verdadero)

# La palabra clave elif te permite verificar multiples condiciones.
# La primera condicion que se evalue como True (verdadero) ejecutara su bloque de codigo, y el resto sera ignorado.
if x > 15:
    print("x es mayor que 15")
elif x > 5:
    print(
        "x es mayor que 5 pero no mayor que 15"
    )  # Este bloque se ejecuta ya que x > 5
else:
    print("x es 5 o menor")

# Sentencias if-else anidadas
# Puedes anidar sentencias if-else entre si para manejar condiciones complejas.
if x > 5:
    if x < 20:
        print("x esta entre 5 y 20")
    else:
        print("x es 20 o mayor")
else:
    print("x es 5 o menor")

# Nota: El uso correcto de la indentacion es fundamental en Python para definir el alcance (scope) de cada bloque.

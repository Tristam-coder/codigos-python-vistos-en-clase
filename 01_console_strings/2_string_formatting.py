# Introduccion a diferentes metodos de formato de cadenas (string formatting).
# Contexto historico (historical context):
# - El formato antiguo (old-style formatting) con '%' existe desde Python 1.x.
# - El metodo str.format() fue introducido en Python 2.7 (July 2010) y Python 3.0 (December 2008).
# - Las f-strings fueron introducidas en Python 3.6 (December 2016).
# Explicación: formatear es aplicar una funcion F(plantilla, valores) -> cadena final.


# 1. Formato antiguo

# Este metodo es similar al formato tipo printf (printf-style formatting) de C.
# '%s' se usa como marcador (placeholder) para strings y '%d' para enteros.
# Explicación: la plantilla recibe el par ordenado (name, age) y produce un string.
name = "Marco"
age = 30
print("Hola, %s. Tienes %d años." % (name, age))
# Salida: Hola, Marco. Tienes 30 años.

# 2. Sintaxis con format()

# Este metodo es mas potente y flexible que el operador '%'.
# Usa llaves {} como marcadores (placeholders), que se reemplazan con los argumentos de format().
# Explicación: format(name, age) sustituye posiciones: {}_1 = name y {}_2 = age.
print("Hola, {}. Tienes {} años.".format(name, age))
# Salida: Hola, Marco. Tienes 30 años.

# 3. F-string

# Las f-strings permiten insertar expresiones dentro de cadenas de forma concisa y legible.
# Se antepone una 'f' a la cadena y se colocan expresiones entre llaves {}.
# Las f-strings se evaluan en tiempo de ejecucion (runtime).
# Explicación: una f-string evalua expresiones y construye F(name, age) = texto.
print(f"Hola, {name}. Tienes {age} años.")
# Salida: Hola, Marco. Tienes 30 años.

# 4. print() con multiples objetos

# La documentacion representa estos argumentos posicionales como *objects.
# print() puede recibir varios objetos separados por comas.
# Por defecto, agrega un espacio entre cada argumento y convierte los valores a texto.
# No es necesario convertir manualmente age con str().
# Explicación: print(a, b, c) muestra str(a) + " " + str(b) + " " + str(c).
print("Hola,", name + ".", "Tienes", age, "años.")
# Salida: Hola, Marco. Tienes 30 años.

# Nota: las f-strings suelen preferirse en Python moderno por legibilidad y eficiencia.

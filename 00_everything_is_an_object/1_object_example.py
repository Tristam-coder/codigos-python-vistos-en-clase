# Cada valor tiene un tipo.
# type() muestra <class 'int'>, <class 'str'>, etc. porque en Python los tipos
# están definidos mediante clases: 10 es un objeto creado por la clase int.
number = 10
# number no “contiene” el 10 como una cajita. Más bien es una etiqueta pegada al objeto 10.
text = "Python"
items = [1, 2, 3]

print("Tipos:")
print("number:", type(number))
print("text:", type(text))
print("items:", type(items))

# Cada objeto tiene una identidad durante su existencia.
# Identidad es un valor único y constante que distingue a un objeto de los demás.
# En CPython, normalmente corresponde a su dirección en memoria.
print("\nIdentidades:")
print("id de number:", id(number))
print("id de text:", id(text))
print("id de items:", id(items))

# Los objetos ofrecen comportamientos según su tipo.
print("\nComportamientos:")
print("10 en binario:", number.bit_length(), "bits")
print("Texto en mayúsculas:", text.upper())

items.append(4)
print("Lista después de append():", items)

# Dos nombres pueden hacer referencia al mismo objeto.
same_items = items

print("\nReferencias:")
print("¿items y same_items tienen el mismo valor?:", items == same_items)
print("¿items y same_items son el mismo objeto?:", items is same_items)

same_items.append(5)
print("items:", items)
print("same_items:", same_items)

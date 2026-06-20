# Simulacion de Bucles Do-While en Python
# Python no tiene un bucle do-while integrado, pero se puede lograr un comportamiento similar usando un bucle while.

# Un bucle do-while garantiza que el cuerpo del bucle se ejecutara al menos una vez antes de verificar la condicion.

# Simulando do-while con un bucle while
count = 0

while True:
    print('Contador:', count)
    count += 1
    if count >= 5:
        break  # Salir del bucle

# Nota: El cuerpo del bucle se ejecuta primero, y la condicion se verifica despues, simulando un bucle do-while.
# Esto es util cuando quieres que el bucle se ejecute al menos una vez independientemente de la condicion.

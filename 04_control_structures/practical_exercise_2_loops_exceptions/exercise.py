total = 0.0

valid_count = 0

attempt_count = 0

while True:

    entrada = input("Ingresa un número o 'salir': ")

    if entrada.lower() == "salir":
        break

    attempt_count += 1

    try:
        num = float(entrada)
        total += num
        valid_count += 1
    except ValueError:
        print("Entrada inválida.")
    finally:
        print("Intento procesado.")

try:
    promedio = total / valid_count
except ZeroDivisionError:
    print("No se ingresaron números válidos.")
else:
    print("Promedio:", promedio)
finally:
    print("Proceso de promedio terminado.")

print("Total:", total)
print("Números válidos:", valid_count)
print("Intentos:", attempt_count)


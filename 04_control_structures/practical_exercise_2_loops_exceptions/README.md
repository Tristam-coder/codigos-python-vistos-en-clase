# Ejercicio práctico 2: repetición y manejo de errores

## Instrucciones

Completa `exercise.py`.

El programa debe pedir números repetidamente. El usuario puede escribir
`salir` para terminar.

Debes utilizar:

- `while True` para repetir el programa;
- `break` para terminar;
- `try` para intentar convertir la entrada a `float`;
- `except ValueError` para manejar entradas no numéricas;
- `finally` para indicar que cada intento fue procesado;
- `try`, `except`, `else` y `finally` para calcular el promedio.

## Reglas

- Los números válidos se acumulan en `total`.
- Cada número válido aumenta `valid_count`.
- Cada entrada distinta de `salir` aumenta `attempt_count`.
- Si no se ingresaron números válidos, debe manejarse la división entre cero.

## Ejemplo de ejecución

```text
Ingresa un número o 'salir': 10
Intento procesado.
Ingresa un número o 'salir': hola
Entrada inválida.
Intento procesado.
Ingresa un número o 'salir': 20
Intento procesado.
Ingresa un número o 'salir': salir
Promedio: 15.0
Proceso de promedio terminado.
Total: 30.0
Números válidos: 2
Intentos: 3
```

El uso de `while True` con una condición de salida al final o durante el bloque
permite simular el comportamiento de un `do-while`.


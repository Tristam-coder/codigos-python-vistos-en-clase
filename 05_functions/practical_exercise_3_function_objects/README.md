# Ejercicio práctico 3: funciones como objetos

## Instrucciones

Completa `exercise.py`.

Este ejercicio reúne los siguientes conceptos:

- función de primer orden;
- función de orden superior;
- función retornada por otra función;
- función pura;
- función impura;
- atributos de una función.

## Reglas

1. `add()` y `multiply()` reciben dos números y devuelven un resultado.
2. `apply_operation()` recibe otra función y la ejecuta.
3. `create_multiplier()` devuelve una nueva función.
4. `calculate_discount()` debe ser pura: no modifica datos externos.
5. `add_to_log()` es impura porque modifica la lista recibida.
6. La función `add()` debe recibir un atributo llamado `description`.

## Salida esperada

```text
Suma: 7
Multiplicación: 12
Doble de 5: 10
Precio con descuento: 90.0
Log: ['Operación completada']
Descripción: Suma dos números
Atributos: {'description': 'Suma dos números'}
```


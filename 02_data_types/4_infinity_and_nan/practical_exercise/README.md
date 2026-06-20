# Ejercicio práctico: infinito y NaN

## Instrucciones

Completa `exercise.py`.

Debes:

1. crear infinito positivo y negativo con `float()`;
2. crear un valor NaN con `float()`;
3. realizar operaciones con infinito;
4. comprobar valores con `math.isinf()` y `math.isnan()`;
5. observar cómo se comporta NaN en una comparación.

## Conceptos importantes

- `inf` representa infinito positivo.
- `-inf` representa infinito negativo.
- `nan` significa *Not a Number*.
- `math.isinf()` comprueba si un valor es infinito.
- `math.isnan()` comprueba si un valor es NaN.
- NaN no es igual a sí mismo.

## Ejemplo de salida

```text
Infinito positivo: inf
Infinito negativo: -inf
NaN: nan
Infinito más 100: inf
Infinito menos infinito: nan
Cero por infinito: nan
¿Es infinito?: True
¿Es NaN?: True
¿NaN es igual a sí mismo?: False
```


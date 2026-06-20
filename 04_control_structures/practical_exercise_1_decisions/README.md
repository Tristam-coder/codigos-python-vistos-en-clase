# Ejercicio práctico 1: decisiones

## Instrucciones

Completa `exercise.py`.

El programa debe solicitar:

- nota final;
- porcentaje de asistencia;
- código de modalidad.

## Clasificación con `if`, `elif` y `else`

- Si la nota es mayor o igual que `11` y la asistencia es mayor o igual que
  `70`, el resultado es `"Aprobado"`.
- Si la nota es mayor o igual que `11`, pero la asistencia es menor que `70`,
  el resultado es `"Inhabilitado por asistencia"`.
- En cualquier otro caso, el resultado es `"Desaprobado"`.

## Modalidad con `match`

- `P`: Presencial
- `V`: Virtual
- `H`: Híbrida
- Cualquier otro código: Desconocida

El código debe funcionar tanto en mayúsculas como en minúsculas.

## Ejemplo de ejecución

```text
Nota final: 15
Asistencia: 85
Modalidad (P/V/H): h
Resultado: Aprobado
Modalidad: Híbrida
```

> `match` requiere Python 3.10 o posterior.


# Ejercicio práctico: conversiones de tipos

## Instrucciones

Completa `exercise.py`.

El programa debe:

1. solicitar una edad y convertirla de `str` a `int`;
2. solicitar una estatura y convertirla de `str` a `float`;
3. sumar un puntaje `int` y una bonificación `float`;
4. convertir la edad de `int` a `str`;
5. convertir una lista de cursos en una tupla;
6. mostrar el valor y el tipo de los resultados.

## Conversión implícita

Al sumar un `int` y un `float`, Python convierte automáticamente el resultado
en `float`.

## Conversión explícita

Cuando utilizas `int()`, `float()`, `str()` o `tuple()`, estás indicando
directamente el tipo que deseas obtener.

## Ejemplo de ejecución

```text
Edad: 20
Estatura en metros: 1.70
Edad convertida: 20 | Tipo: <class 'int'>
Estatura convertida: 1.7 | Tipo: <class 'float'>
Puntaje final: 17.5 | Tipo: <class 'float'>
Mensaje: Edad: 20 | Tipo: <class 'str'>
Cursos: ('Python', 'Git') | Tipo: <class 'tuple'>
```


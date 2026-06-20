# Ejercicio práctico 1: funciones básicas

## Instrucciones

Completa `exercise.py`.

Debes crear funciones para calcular y mostrar la información de una compra.

## Funciones

### `calculate_subtotal(price, quantity)`

Recibe el precio y la cantidad. Devuelve su multiplicación.

### `calculate_tax(subtotal, tax_rate=0.18)`

Recibe el subtotal y un porcentaje opcional. Devuelve el impuesto.

### `calculate_total(subtotal, tax)`

Recibe el subtotal y el impuesto. Devuelve su suma.

### `show_receipt(product, subtotal, tax, total)`

Recibe los datos de la compra y los muestra. Esta función no necesita devolver
un valor.

## Ejemplo de salida

```text
Producto: Cuaderno
Subtotal: 30.0
Impuesto: 5.3999999999999995
Total: 35.4
Impuesto personalizado: 3.0
```

El impuesto personalizado debe calcularse llamando a `calculate_tax()` con
`0.10` como segundo argumento.


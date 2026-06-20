# En Python, todo valor es un objeto

En Python, cada valor que utilizamos es un objeto. Un objeto tiene:

- un **tipo**, que se puede consultar con `type()`;
- una **identidad**, que se puede consultar con `id()`;
- un **valor**;
- comportamientos disponibles mediante métodos.

Por ejemplo, el número `10` es un objeto de tipo `int` y el texto `"Python"`
es un objeto de tipo `str`.

```python
number = 10
text = "Python"

print(type(number))
print(type(text))
```

Salida:

```text
<class 'int'>
<class 'str'>
```

## Las variables son nombres

Una variable no contiene literalmente el objeto. Es un nombre que hace
referencia a un objeto.

```python
first_name = "Ana"
other_name = first_name
```

En este ejemplo, ambos nombres hacen referencia al mismo objeto:

```python
print(first_name is other_name)
```

Salida:

```text
True
```

El operador `is` compara la identidad de dos objetos. No debe utilizarse para
comparar normalmente números o cadenas; para comparar sus valores se usa `==`.

## ¿Qué significa “todo es un objeto”?

Los números, cadenas, listas, funciones, clases, módulos y hasta los propios
tipos pueden tratarse como valores y son objetos.

Los nombres de variables, palabras reservadas y operadores forman parte de la
sintaxis del lenguaje; no son valores almacenados en una variable.

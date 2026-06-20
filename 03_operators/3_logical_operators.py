# Operadores logicos (logical operators) en Python.
# Version de Python (Python Version): existen desde Python 1.0 (January 1994).

# Los operadores logicos combinan varias condiciones y devuelven un booleano (boolean).
# Explicación: trabajan en algebra booleana con valores {True, False}.

# and - Devuelve True si ambos operandos (operands) son verdaderos.
# Explicación: and es conjuncion; p and q es True solo si p = True y q = True.
print('True and False:', True and False)  # Salida (output): False

# or - Devuelve True si al menos un operando es verdadero.
# Explicación: or es disyuncion inclusiva; p or q es True si p = True o q = True.
print('True or False:', True or False)  # Salida: True

# not - Invierte el valor booleano.
# Explicación: not es negacion; not True = False y not False = True.
print('not True:', not True)  # Salida: False

# Nota: son esenciales en el flujo de control (control flow)
# porque permiten decisiones mas complejas en condiciones (conditions).

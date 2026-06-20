# Operadores bit a bit (bitwise operators) en Python.
# Version de Python (Python Version): existen desde Python 1.0 (January 1994).

# Los operadores bitwise realizan operaciones sobre la representacion binaria de enteros.
# Tratan los numeros como una secuencia de bits (binary digits), no como decimales o hexadecimales.
# Las operaciones principales son AND, OR, XOR, NOT y desplazamientos (bit shifts).
# Explicación: un entero se representa como suma de bits: n = suma(bit_i * 2^i).

# Entender numeros binarios (binary numbers):
# El sistema binario usa dos simbolos, 0 y 1. Cada digito binario se llama bit.
# Por ejemplo, 1100 representa el decimal 12 y 1010 representa el decimal 10.
# Explicación: 1100_2 = 1*2^3 + 1*2^2 + 0*2^1 + 0*2^0 = 12.
# Explicación: 1010_2 = 1*2^3 + 0*2^2 + 1*2^1 + 0*2^0 = 10.

# Asignar valores binarios a variables:
a = 0b1100  # Binario (binary) para 12
b = 0b1010  # Binario para 10

# Nota: las operaciones bitwise funcionan igual si los numeros vienen en binario,
# decimal o hexadecimal.
# Por ejemplo, estas operaciones con enteros decimales darian los mismos resultados:
# a = 12  # Decimal para 0b1100
# b = 10  # Decimal para 0b1010

# Operador AND (&):
# El operador AND bit a bit (bitwise AND) compara cada bit de sus operandos.
# Si ambos bits son 1, el bit resultante es 1; si no, es 0.
# Explicación: para cada bit, AND equivale a multiplicacion booleana: 1 & 1 = 1, si no 0.
# Tabla de verdad (truth table) para AND:
#   a  b  a & b
#   0  0    0
#   0  1    0
#   1  0    0
#   1  1    1
print('a & b:', bin(a & b))  # Salida (output): 0b1000 (binario para 8)

# Operador OR (|):
# El operador OR bit a bit (bitwise OR) compara cada bit de sus operandos.
# Si al menos un bit es 1, el bit resultante es 1; si no, es 0.
# Explicación: para cada bit, OR devuelve max(bit_a, bit_b).
# Tabla de verdad (truth table) para OR:
#   a  b  a | b
#   0  0    0
#   0  1    1
#   1  0    1
#   1  1    1
print('a | b:', bin(a | b))  # Salida: 0b1110 (binario para 14)

# Operador XOR (^):
# El operador XOR bit a bit (exclusive OR) compara cada bit de sus operandos.
# Si los bits son diferentes, el bit resultante es 1; si son iguales, es 0.
# Explicación: XOR equivale a suma modulo 2: bit_a xor bit_b = (bit_a + bit_b) mod 2.
# Tabla de verdad (truth table) para XOR:
#   a  b  a ^ b
#   0  0    0
#   0  1    1
#   1  0    1
#   1  1    0
print('a ^ b:', bin(a ^ b))  # Salida: 0b0110 (binario para 6)

# Operador NOT (~):
# El operador NOT bit a bit (bitwise NOT) es un operador unario (unary operator)
# que invierte todos los bits de su operando: 0 pasa a 1 y 1 pasa a 0.
# En Python tambien considera el signo del entero y usa complemento a dos (two's complement).
# Formula: ~x = -x - 1
# Explicación: para a = 12, ~a = -12 - 1 = -13.
print('~a:', bin(~a))  # Salida: -0b1101 (binario para -13)

# Operador de desplazamiento a la izquierda (left shift, <<):
# Desplaza los bits del primer operando hacia la izquierda por las posiciones indicadas.
# Cada desplazamiento multiplica por 2. Los bits que salen se descartan y a la derecha entran 0s.
# Por ejemplo, 0b1100 (12) desplazado 2 posiciones produce 0b110000 (48).
# Explicación: a << k equivale a a * 2^k; 12 << 2 = 12 * 4 = 48.
print('a << 2:', bin(a << 2))  # Salida: 0b110000 (binario para 48)

# Operador de desplazamiento a la derecha (right shift, >>):
# Desplaza los bits del primer operando hacia la derecha por las posiciones indicadas.
# Cada desplazamiento divide por 2 usando division entera (integer division).
# Los bits que salen se descartan; a la izquierda entra el bit de signo o 0, segun el caso.
# Por ejemplo, 0b1100 (12) desplazado 2 posiciones produce 0b0011 (3).
# Explicación: a >> k equivale a floor(a / 2^k) para enteros no negativos; 12 >> 2 = 3.
print('a >> 2:', bin(a >> 2))  # Salida: 0b0011 (binario para 3)

# Nota: tambien puedes hacer estas operaciones directamente con enteros,
# sin convertirlos primero a binario:
# print("a & b:", a & b)  # Salida: 8
# print("a | b:", a | b)  # Salida: 14
# print("a ^ b:", a ^ b)  # Salida: 6
# print("~a:", ~a)        # Salida: -13
# print("a << 2:", a << 2)  # Salida: 48
# print("a >> 2:", a >> 2)  # Salida: 3

# Las operaciones bitwise se usan en programacion de bajo nivel (low-level programming),
# criptografia, protocolos de red y optimizacion de rendimiento.
# Permiten manipular datos eficientemente a nivel de bit (bit level).

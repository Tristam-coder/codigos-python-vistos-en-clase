# Recursion de funciones (functions) en Python
# NOTA: La recursion es un metodo donde una funcion se llama a si misma
# para resolver instancias mas pequenas del mismo problema.
# Util para problemas que se pueden dividir en subproblemas similares.


def factorial(n):
    # Caso base (base case): si n es 1 o 0, retornar 1 (ya que 0! = 1 y 1! = 1)
    if n == 1 or n == 0:
        return 1
    # Caso recursivo (recursive case): n * factorial de n-1
    else:
        return n * factorial(n - 1)


result = factorial(5)
print('Factorial de 5:', result)  # Salida (output): Factorial de 5: 120

# La clave para entender la recursion es reconocer el caso base, que detiene
# la recursion, y el caso recursivo, que reduce el problema en subproblemas
# mas pequenos.


def fibonacci(n):
    # Caso base (base case): F(0) = 0, F(1) = 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Caso recursivo (recursive case): F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fib_result = fibonacci(6)
# Salida (output): 6to numero de Fibonacci: 8
print('6to numero de Fibonacci:', fib_result)

# NOTA: La recursion es elegante y simplifica problemas que tienen una
# estructura recursiva natural.
# Sin embargo, debe usarse con cuidado ya que una recursion profunda
# puede causar problemas de rendimiento, como uso excesivo de memoria
# o alcanzar el limite de recursion.

# Las soluciones iterativas suelen preferirse para problemas a gran escala
# por razones de eficiencia.

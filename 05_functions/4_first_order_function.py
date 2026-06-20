# Las funciones de primer orden (first-order) son funciones que NO reciben
# otras funciones como argumentos ni retornan funciones.

def add(a, b):
    return a + b


# Esta funcion es una funcion de primer orden (first-order) porque opera
# directamente sobre sus argumentos sin involucrar ninguna otra funcion.
print(add(3, 4))  # Salida (output): 7


# En contraste, la siguiente funcion no es una funcion de primer orden
# (first-order) porque recibe otra funcion como argumento.
def apply(func, a, b):
    return func(a, b)

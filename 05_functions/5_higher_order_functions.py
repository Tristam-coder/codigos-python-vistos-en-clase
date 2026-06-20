# Las funciones de orden superior son funciones que reciben otras funciones como
# argumentos y/o retornan funciones.

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


# La siguiente funcion es una funcion de orden superior porque recibe
# otra funcion como argumento.

def apply_operation(a, b, operation):
    # Esta funcion recibe otra funcion como argumento (operation)
    # y la aplica a los argumentos dados a y b.
    return operation(a, b)


# Usando la funcion apply_operation con diferentes operaciones
result_add = apply_operation(3, 4, add)
print(result_add)  # Salida (output): 7

result_multiply = apply_operation(5, 6, multiply)
print(result_multiply)  # Salida (output): 30


###############################################


# Las funciones de orden superior tambien pueden retornar otras funciones.
# Aqui hay un ejemplo de una funcion de orden superior que retorna una funcion.

def create_multiplier(n):
    # Esta funcion retorna una nueva funcion que multiplica su entrada por n.
    def multiplier(x):
        return x * n
    return multiplier


# Usando la funcion de orden superior para crear nuevas funciones
double = create_multiplier(2)
triple = create_multiplier(3)

# Las funciones double y triple son creadas por la funcion de orden superior
# create_multiplier y pueden ser usadas independientemente.

print(double(5))  # Salida (output): 10
print(triple(5))  # Salida (output): 15

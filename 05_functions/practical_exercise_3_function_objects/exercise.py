def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def apply_operation(a, b, operation):
    return operation(a, b)

def create_multiplier(multiplier):
    def multiply_value(value):
        return value * multiplier
    return multiply_value

def calculate_discount(price, discount):
    return price - price * discount

def add_to_log(message, log):
    log.append(message)

sum_result = apply_operation(3, 4, add)

multiplication_result = apply_operation(3, 4, multiply)

double = create_multiplier(2)

double_result = double(5)

discounted_price = calculate_discount(100, 0.10)

operation_log = []

add_to_log("Operación completada", operation_log)

add.description = "Suma dos números"

print("Suma:", sum_result)
print("Multiplicación:", multiplication_result)
print("Doble de 5:", double_result)
print("Precio con descuento:", discounted_price)
print("Log:", operation_log)
print("Descripción:", add.description)
print("Atributos:", add.__dict__)


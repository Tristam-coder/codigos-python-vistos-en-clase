def calculate_subtotal(price, quantity):
    return price * quantity

def calculate_tax(subtotal, tax_rate=0.18):
    return subtotal * tax_rate

def calculate_total(subtotal, tax):
    return subtotal + tax

def show_receipt(product, subtotal, tax, total):
    print("Producto:", product)
    print("Subtotal:", subtotal)
    print("Impuesto:", tax)
    print("Total:", total)

product = "Cuaderno"

subtotal = calculate_subtotal(7.5, 4)

tax = calculate_tax(subtotal)

total = calculate_total(subtotal, tax)

show_receipt(product, subtotal, tax, total)

custom_tax = calculate_tax(subtotal, 0.10)

print("Impuesto personalizado:", custom_tax)


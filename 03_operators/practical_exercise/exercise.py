price = 12.5

quantity = 8

available_money = 120

subtotal = price * quantity

change = available_money - subtotal

complete_boxes = quantity // 3

remaining_units = quantity % 3

power = 2 ** 3

has_enough_money = available_money >= subtotal

is_large_purchase = quantity > 5

is_exact_payment = available_money == subtotal

is_approved = has_enough_money and quantity > 0

requires_review = not is_approved or subtotal >= 500

stock = 20

stock -= quantity

stock += 2

print("Subtotal:", subtotal)

print("Vuelto:", change)

print("Cajas completas:", complete_boxes)

print("Unidades sobrantes:", remaining_units)

print("Potencia:", power)

print("¿Tiene dinero suficiente?:", has_enough_money)

print("¿Es una compra grande?:", is_large_purchase)

print("¿El pago es exacto?:", is_exact_payment)

print("¿La compra está aprobada?:", is_approved)

print("¿Requiere revisión?:", requires_review)

print("Stock final:", stock)

def countdown(number):
    if number <= 0:
        print("Fin")
        return
    print(number)
    countdown(number - 1)

def sum_to(number):
    if number <= 0:
        return 0
    return number + sum_to(number - 1)

countdown(5)

total = sum_to(5)

print("Suma de 1 a 5:", total)


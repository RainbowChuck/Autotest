# --------------------------Применение условий---------------

def sum_one_to_hundred():
    sum = 0
    for i in range(101):
        if i % 2 == 0:
            sum += i
    return sum
print(sum_one_to_hundred())

odds = [x ** 2 for x in range(11) if x % 2 != 0]


def strange_function():
    counter = 0
    try:
        while int(input("Введите число, отрицательное, чтобы остановиться: ")) > 0:
            counter += 1
    except (ValueError, TypeError):
        print("Только инты")
    return counter

print(odds)
print(strange_function())
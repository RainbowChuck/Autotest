def one_to_five(number):
    numbers = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}
    if isinstance(number, int) and number in numbers:
        return numbers[number]
    else:
        print("Только инты от 1 до 5")

print(one_to_five(3))
print(one_to_five("v"))
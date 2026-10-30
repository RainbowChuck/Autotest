def one_to_five(number):
    if isinstance(number, int):
        numbers = {1 : "One", 2 : "Two", 3 : "Three", 4 : "Four", 5 : "Five"}
        return numbers[number]
    else:
        print("Только инты")

print(one_to_five(3))
print(one_to_five("v"))
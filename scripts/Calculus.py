answer = "n"
while answer != "quit":
    result = 0
    try:
        first_num = float(input("Please enter your first number: "))
        second_num = float(input("Please enter your second number: "))
        operation = input("Enter operation from: +,-,/,*")
        if operation == "+":
            result = first_num + second_num
            print("sum result:")
        elif operation == "-":
            result = first_num - second_num
            print("subtraction result:")
        elif operation == "/":
            result = first_num / second_num
            print("division result:")
        elif operation == "*":
            result = first_num * second_num
            print("multiplication result:")
    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
        print("Please enter a number, not a zero")
    finally:
        print(result)
        print("Thanks for using calculus...")
        answer = input("If you want to quit: quit")
try:
    first = int(input("Please enter your first number: "))
    second = int(input("Please enter your second number: "))
    result = 0
    result = first/second
    print(result)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("You've entered an invalid number")
finally:
    print("Thank you for using this program. Well, it died")
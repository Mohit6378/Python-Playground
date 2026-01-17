try:
    num = int(input("Enter a number: "))
    try:
        result = 10 / num
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print("Result: ", result)
except ValueError:
    print("You are told to enter a number.")
finally:
    print("Program finished (resources closed)")
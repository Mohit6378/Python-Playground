try:
    num = int(input("Enter a number."))
    result = 10 / num
    print("Result: ", result)
except ZeroDivisionError as e:
    print("Cannot divide by zero.")
except ValueError:
    print("You are told to enter a number!")

print("Program finished.")
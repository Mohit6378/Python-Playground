try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result: ", result)
except ZeroDivisionError:
    print("You cannot divide by zero!")

print("Program finished.")
try:
    num = int(input("Enter a number. "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("you are told to enter a number.")
else:
    print("Result: ", result)
finally:
    print("Program finished. (Resources closed)")
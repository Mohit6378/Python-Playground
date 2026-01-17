try:
    num = int(input("Enter a number. "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("You are told to enter a number.")
except Exception as e:
    print("Error occured: ", e)
else:
    print("Result: ", result)

print("Program finished.")
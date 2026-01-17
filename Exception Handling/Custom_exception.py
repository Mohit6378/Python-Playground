class NegativeNumberException(Exception):
    pass

def sqrt(num):
    if num < 0:
        raise NegativeNumberException("square root of negative number is not possible.")
    return num ** 0.5

try:
   num = sqrt(int(input("Enter a number to find its square root: ")))
except NegativeNumberException as e:
    print("Error occurred: ", e)
else:
    print("square root is: ", num)
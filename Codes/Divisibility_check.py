#fuction for divisibility check
def is_divisible(a, b):
    return a % b == 0     #returns either true or false

#taking input from user
a = float(input("Enter the number you want to divide.\n"))
b = float(input("Enter the number you want to divide by\n"))

#printing result
if is_divisible(a,b):
    print(f"{a} is completely divisible by {b}")
else:
    print(f"{a} is not divisible by {b}")

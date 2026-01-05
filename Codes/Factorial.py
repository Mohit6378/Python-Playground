#factorial function
def factorial(num):
    # fact = 0
    if num<=1:
        return 1
    else:
       return num*factorial(num-1)
    
num = int(input("Enter an integer to find its factorial.\n"))
print(f"Factorial of {num} is: {factorial(num)}")
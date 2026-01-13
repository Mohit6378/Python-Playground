def fibonacci(term):
    if term <-0:
        return "Invalid input."
    elif term == 1:
        return 0
    elif term == 2:
        return 1
    else:
        return fibonacci(term-1) + fibonacci(term-2)

term = int(input("Enter number of terms you want to print: "))
for i in range(1, term + 1):
    print(fibonacci(i), end = "  ")
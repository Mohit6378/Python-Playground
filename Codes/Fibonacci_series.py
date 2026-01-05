def fibonacci_series(num):
    a,b = 0,1
    for i in range(num):
        print(a, end=" ")
        a,b = b,a+b

num = int(input("Enter number of terms of fibonacci series\n"))
fibonacci_series(num)
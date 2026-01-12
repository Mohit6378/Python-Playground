#logic to find factors
def factor(num):
    for i in range(1,int(num**0.5)+1):
        if num % i == 0:
            print(i, end = ", ")
            if i != num // i:
                print(num // i, end = ", ")
#taking input
num = int(input("Enter a number to find its factor.\n"))
print("Factors: ", end = "")
factor(num)
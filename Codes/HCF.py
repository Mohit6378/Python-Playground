#logic for Euclidean algo
def hcf(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1
#Taking input
num1 = int(input("Enter 1st number.\n"))
num2 = int(input("Enter 2nd number.\n"))
#printing HCF
print("HCF of both the number is:",hcf(num1,num2))
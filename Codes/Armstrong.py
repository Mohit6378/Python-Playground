def armstrong_num(num):
    length = len(str(num))
    arm = sum(int(digit) ** length for digit in str(num))
    return arm == num

num = int(input("Enter a number\n"))
if armstrong_num(num):
    print(f"{num} is an armstrong number")
else:
    print(f"{num} is not an armstrong number")

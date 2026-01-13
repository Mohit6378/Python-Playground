def natural_sum(num):
    if num < 1:
        return "Enter a valid natural number."
    elif num == 1:
        return 1
    else:
        return num + natural_sum(num - 1)

num = int(input("Enter a natural number: "))
print(f"Sum of {num} natural numbers is: {natural_sum(num)}")
def decimal_binary(num):
    if num == 0:
        return ""
    else:
        return decimal_binary(num // 2) + str(num % 2)

decimal = int(input("Enter a number to convert in binary: "))
print("Binary form: ", decimal_binary(decimal))
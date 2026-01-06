decimal = int(input("Enter an integer to convert.\n"))
print(f"conversion of {decimal} to other number system:")

#printing in other number systems without prefix of that number.
print(bin(decimal)[2:],"in binary")
print(oct(decimal)[2:],"in octal")
print(hex(decimal)[2:],"in hexadecimal")
height = int(input("Enter the height of triangle: "))
#spacing logic
for i in range(height):
    for j in range(height - i - 1):
        print(" ", end = "")
#characters logic
    ch = 65
    for k in range((2 * i) + 1):
        print(chr(ch), end = "")
        if (k < i):
            ch += 1
        else:
            ch -= 1
    print()

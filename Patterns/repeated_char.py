height = int(input("Enter the height of triangle: "))
for i in range(height):
    for j in range(i + 1):
        print(chr(65 + (i % 26)), end = " ")
    print()
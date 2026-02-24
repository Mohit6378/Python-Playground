height = int(input("Enter the height of triangle: "))
for i in range(height):
    for j in range(height - i):
        print(chr(65+ (j % 26)), end = " ")
    print()
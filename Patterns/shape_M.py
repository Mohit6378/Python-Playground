height = int(input("Enter the height of triangle: "))
for i in range(1, height + 1):
    for j in range(1, i + 1):
        print(j, end = " ")
    for k in range((2 * height) - (i * 2)):
        print(" ", end = " ")
    for l in range(i, 0, -1):
        print(l, end = " ")
    print()
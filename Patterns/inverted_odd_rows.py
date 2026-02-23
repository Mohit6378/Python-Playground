height = int(input("Enter the height of triangle: "))
for i in range(height - 1, -1, -1):
    for k in range(height - i -1):
        print(" ", end = "")

    for j in range((2 * i) + 1):
        print("*", end = "")
    print()

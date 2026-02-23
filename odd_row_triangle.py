height = int(input("Enter the height of triangle: "))
for i in range(height):
    for j in range((height - 1) - i):
        print(" ", end = "")
    for k in range((2 * i) + 1):
        print("*", end = "")
    print()
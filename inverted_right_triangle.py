height = int(input("Enter the height of triangle: "))
while (height > 0):
    for i in range(1, height + 1):
        print("*", end = "")
    print()
    height -= 1
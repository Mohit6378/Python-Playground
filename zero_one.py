height = int(input("Enter the height of triangle: "))
for i in range(1, height + 1):
    start = 1 if (i % 2 != 0) else 0
    for j in range(i):
        print(start, end = "")
        start = 1 - start
    print()

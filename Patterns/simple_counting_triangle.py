height = int(input("Enter the height of triangle: "))
k = 1
for i in range(1, height + 1):
    for j in range(i):
        print(k, end = " ")
        k += 1
    print()
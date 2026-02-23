star = int(input("Enter maximum number of stars: "))
for i in range(1, (2 * star)):
    n = i
    if (i > star):
        n = (2 * star) - i
    for j in range(n):
        print("*", end = "")
    print()
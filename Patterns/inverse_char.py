height = int(input("Enter the height of triangle: "))
for i in range(height):
    start_char = chr(64+(height - i))
    for j in range(i + 1):
        print(chr(ord(start_char) + j), end = "")
    print()

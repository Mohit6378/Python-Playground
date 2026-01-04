values = [int(x) for x in input("Enter three numbers separated by space\n").split()]
if (values[0]>values[1] and values[0]>values[2]):
    print(values[0],"is the largest")
elif (values[1]>values[0] and values[1]>values[2]):
    print(values[1],"is the largest")
else:
    print(values[2],"is the largest.")

# we can use max() function too
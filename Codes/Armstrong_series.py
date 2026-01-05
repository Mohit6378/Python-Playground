def armstrong_series(start, end):
    armstrong_nums = []
    for i in range(start, end+1):
        #finding number of digits
        length = len(str(i))
        #calculating sum of digits raised to the power of number of digits
        total = sum(int(digit) ** length for digit in str(i))
        #adding to list if armstrong
        if total == i:
            armstrong_nums.append(i)
    
    if armstrong_nums:
        print(f"Armstrong number between {start} and {end} are: {' '.join(map(str, armstrong_nums))}")
    else:
        print("No armstrong numbers in this interval")

start = int(input("Enter starting point of armstrong series.\n"))
end = int(input("Enter ending point of armstrong series.\n"))
armstrong_series(start, end)

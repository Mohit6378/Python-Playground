#Taking accurate input from the user.
nums = list(map(int, input("Enter end points of interval:\n").split()))
if (len(nums)==2):
    a,b = nums
else:
    print("Enter exactly two end points.")
    exit()
#logic to find prime numbers in the given interval.
prime_list = []
for i in range(a,b+1):
    if i<2:
        continue
    for j in range(2,int(i**0.5)+1):
        if (i%j==0):
            break
    else:
        prime_list.append(i)
#printing the list of prime numbers in given interval.
print(prime_list)
#Taking number of terms we want in the list as input.
nterms = int(input("Enter number of terms.\n"))
power_of_two = [1]    #start with 2^0

#logic for creating a list of power of two's of given terms.
for _ in range(1,nterms):
    power_of_two.append(power_of_two[-1] * 2)

#printing list.
print(power_of_two)
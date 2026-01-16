#define two sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("Set A: ", A)
print("Set B: ", B)

#Union (all elements from both sets)

print("Union (A U B): ", A | B)

#Intersection (common elements)

print("Intersection (A ∩ B): ", A & B)

#Difference (Elements in A but not in B)

print("Difference (A - B): ", A - B)

#Symmetric Difference (elements in A or B but not both)

print("Symmetric difference (A ^ B): ", A ^ B)

#Subset and superset check

print("Is A subset of B? ", A.issubset(B))
print("Is A superset of B? ", A.issuperset(B))
def transpose(a):
    result = [[a[col][row] for col in range(len(a))] for row in range(len(a[0]))]
    return result

A = [[1, 2],
     [4, 5],
     [7, 8]]
A_trans = transpose(A)
for row in A_trans:
    print(row)
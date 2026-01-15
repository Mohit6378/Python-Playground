def matrix_sum(a,b):
    result = [[0 for _ in range(len(a[i]))] for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[i])):
            result[i][j] = a[i][j] + b[i][j]
    return result

A = [[11, 4, 7],
     [4, 14, 1],
     [1, 10, 2]]
B = [[5, 3, 11],
     [4, 15, 6],
     [3, 1, 16]]

C = matrix_sum(A, B)
print("Addition of matrix is: ")
for row in C:
    print(row)
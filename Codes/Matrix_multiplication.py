def matrix_multiply(a, b):
    #cols and rows of matrix a and b
    row_a = len(a)
    row_b = len(b)
    col_a = len(a[0])
    col_b = len(b[0])

    #checking if matrix multiplication is possible or not.
    if (col_a != row_b):
        raise ValueError("Number of columns in A is not equal to number of rows in B.")

    #creating a matrix of size col_a X row_b
    result = [[0 for _ in range(col_b)] for _ in range(row_a)]

    #matrix multiplication
    for i in range(row_a):
        for j in range(col_b):
            for k in range(col_a):
                result[i][j] += a[i][k] * b[k][j]
    
    return result

A = [[1, 2],
     [3, 4],
     [5, 6]]
B = [[6, 5, 4],
     [3, 2, 1]]

result = matrix_multiply(A, B)
print("Multiplication of both matrices is: ")
for row in result:
    print(row)
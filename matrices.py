A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

def matrix_addition(A, B):
    result = []

    for i in range(2):
        row = []
        for j in range(2):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result

def dot_product(A, B):
    result = []

    for i in range(2):
        row = []
        for j in range(2):
            sum_product = 0
            for k in range(2):
                sum_product += A[i][k] * B[k][j]
            row.append(sum_product)
        result.append(row)
    return result


print("Matrix Addition", matrix_addition(A, B))
print("Dot Product:", dot_product(A, B))


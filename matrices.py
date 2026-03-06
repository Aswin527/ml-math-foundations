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


def matrix_multiplication(A,B):
    result = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += A[i][k] * B[k][j]
    return result

print("Matrix Addition", matrix_addition(A, B))
print("Matrix Multiplication:",matrix_multiplication(A,B))


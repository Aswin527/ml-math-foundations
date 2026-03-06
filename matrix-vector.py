A=[[1,2],[3,4]]
B=[5,6]

result=[0,0]

for i in range(2):
    for j in range(2):
        result [i] += A[i][j]*B[j]
    
print(result)
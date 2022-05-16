import sys
input=sys.stdin.readline

def mat_squ(matrix):
    n=len(matrix)
    ret=[]
    for i in range(n):
        tmp=[]
        for j in range(n):
            tmp.append(sum(matrix[i][k]*matrix[k][j] for k in range(n))%1000)
        ret.append(tmp)
    return ret

def mat_mul(matrix1, matrix2):
    n=len(matrix1)
    ret=[]
    for i in range(n):
        tmp=[]
        for j in range(n):
            tmp.append(sum(matrix1[i][k]*matrix2[k][j] for k in range(n))%1000)
        ret.append(tmp)
    return ret

matrix=[]
n, m=map(int,input().split())
for i in range(n):
    tmp=list(map(int, input().split()))
    matrix.append(tmp)

def fast_square(matrix, m):
    if m==1:
        return matrix
    else:
        if m%2:
            return mat_mul(fast_square(matrix, m-1), matrix)
        else:
            return mat_squ(fast_square(matrix, m//2))

matrix=fast_square(matrix, m)

for i in range(n):
    for j in range(n):
        if matrix[i][j]>=1000:
            matrix[i][j]%=1000

for i in matrix:
    print(*i)

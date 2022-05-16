import sys
input=sys.stdin.readline

row, col=map(int, input().split())

ma=[]
mb=[]
matrix=[]

if row!=0 and col!=0:
    for i in range(row):
        tmp=list(map(int, input().split()))
        ma.append(tmp)

row, col=map(int, input().split())

if row!=0 and col!=0:
    for i in range(row):
        tmp=list(map(int, input().split()))
        mb.append(tmp)

for i in range(len(ma)):
    tmp=[]
    for j in range(len(mb)):
        tmp.append(sum(ma[i][k]*mb[k][j] for k in range(len(ma[0]))))
    matrix.append(tmp)
for i in matrix:
    print(*i)


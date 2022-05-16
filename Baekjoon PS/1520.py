import sys
input=sys.stdin.readline

def counting_sort(lst):
    a={i:[] for i in range(10000, 0, -1)}
    ret=[]
    for i in range(len(lst)):
        a[lst[i][0]].append(lst[i][1])
    for i in a:
        ret.extend(a[i])
    return ret

n, m=map(int, input().split())
mat=[[0 for i in range(m)] for j in range(n)]
inp=[]
sort=[]
for i in range(n):
    tmp=list(map(int, input().split()))
    inp.append(tmp)
    sort.extend(tmp)
for i in range(len(sort)):
    sort[i]=[sort[i], (i//m, i%m)]

sort=counting_sort(sort)
mat[0][0]=1
for pos in sort:
    y=pos[0]
    x=pos[1]
    if x>=1 and inp[y][x]>inp[y][x-1]:
        mat[y][x-1]+=mat[y][x]
    if x+1<m and inp[y][x]>inp[y][x+1]:
        mat[y][x+1]+=mat[y][x]
    if y>=1 and inp[y][x]>inp[y-1][x]:
        mat[y-1][x]+=mat[y][x]  
    if y+1<n and inp[y][x]>inp[y+1][x]:
        mat[y+1][x]+=mat[y][x]

print(mat[-1][-1])

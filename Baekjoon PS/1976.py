import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

def union(a, b):
    a=find(a)
    b=find(b)
    uf[a]=uf[b]
def find(a):
    if uf[a]==a:
        return a
    else:
        uf[a]=find(uf[a])
        return uf[a]


n=int(input())
m=int(input())
uf=[i for i in range(n)]
for i in range(n):
    tmp=list(map(int, input().split()))
    for j in range(n):
        if tmp[j]==1:
            union(i, j)
ok=[0 for i in range(n)]
schedule=list(map(lambda x: int(x)-1, input().split()))
if schedule:
    ans=find(schedule[0])
fail=0
for i in schedule:
    if ok[i]==1:
        continue
    else:
        ok[i]=1
    if ans!=find(i):
        fail=1
        break
if fail:
    print('NO')
else:
    print('YES')
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


n, m=map(int, input().split())
uf=[i for i in range(n+1)]
for i in range(m):
    command, a, b=map(int ,input().split())
    if command:
        a=find(a)
        b=find(b)
        if a==b:
            print('YES')
        else:
            print('NO')
    else:
        union(a, b)
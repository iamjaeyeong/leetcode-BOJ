import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)
def find(a):
    if a==uf[a]:
        return a
    else:
        uf[a]=find(uf[a])
        return uf[a]

def union(a, b):
    uf[a]=uf[b]

n, m=map(int, input().split())
uf=[i for i in range(n)]
idx=0
for i in range(m):
    a,b=map(int, input().split())
    t1=find(a)
    t2=find(b)
    if t1==t2:
        idx=i+1
        break
    else:
        union(t1 ,t2)
print(idx)

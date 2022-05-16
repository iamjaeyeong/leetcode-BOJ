import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

def find(a):
    if node[a]==a:
        return a
    else:
        cnt[node[a]]+=cnt[a]
        cnt[a]=0
        node[a]=find(node[a])
        return node[a]

def union(a, b):
    a=find(a)
    b=find(b)
    node[a]=node[b]

t=int(input())
for i in range(t):
    n=int(input())
    node={}
    cnt={}
    for i in range(n):
        a, b=input().rstrip().split()
        if a not in node:
            cnt[a]=1
            node[a]=a
        if b not in node:
            cnt[b]=1
            node[b]=b
        union(a, b)
        print(cnt[find(a)])

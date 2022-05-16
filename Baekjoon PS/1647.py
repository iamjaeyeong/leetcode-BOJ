import sys
input=sys.stdin.readline

def find(a):
    if uf[a]==a:
        return a
    else:
        uf[a]=find(uf[a])
        return uf[a]

def union(a, b):
    a=find(a)
    b=find(b)
    uf[a]=uf[b]

n, m=map(int, input().split())
road=[]
ans=0
uf=[i for i in range(n)]
for i in range(m):
    a, b, cost=map(int, input().split())
    road.append([a-1, b-1, cost])
road.sort(key=lambda x:x[-1])
cnt=0
for a, b, cost in road:
    if cnt==n-2:
        break
    if find(a)==find(b):
        continue
    else:
        union(a, b)
        ans+=cost
        cnt+=1

print(ans)


    
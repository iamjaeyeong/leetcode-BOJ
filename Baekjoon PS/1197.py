import sys, heapq
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

v, e=map(int, input().split())
edges=[]
uf=[i for i in range(v)]
finished=[0 for i in range(v)]
for i in range(e):
    a ,b, c=map(int, input().split())
    heapq.heappush(edges, [c, a-1, b-1])
ans=0
while edges:
    edge=heapq.heappop(edges)
    if find(edge[1])==find(edge[2]):
        continue
    else:
        union(edge[1], edge[2])
        ans+=edge[0]
print(ans)
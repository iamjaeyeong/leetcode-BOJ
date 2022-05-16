import sys, heapq
input=sys.stdin.readline

def union(a, b):
    a=find(a)
    b=find(b)
    uf[a]=uf[b]

def find(a):
    if a==uf[a]:
        return a
    else:
        uf[a]=find(uf[a])
        return uf[a]

def distance(p1, p2):
    return pow((p1[0]-p2[0])**2+(p1[1]-p2[1])**2, 1/2)

stars=int(input())
pos=[]
for i in range(stars):
    pos.append(list(map(float, input().split())))
uf=[i for i in range(stars)]

heap=[]
for i in range(stars):
    for j in range(stars):
        heapq.heappush(heap, (distance(pos[i], pos[j]), i, j))
ans=0
while heap:
    d, a, b=heapq.heappop(heap)
    if find(a)==find(b):
        continue
    else:
        union(a, b)
        ans+=d
print('%0.2f'%ans)


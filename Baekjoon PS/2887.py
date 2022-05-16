import sys, heapq
from tkinter import E
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

n=int(input())
pos=[]
for i in range(n):
    tmp=list(map(int, input().split()))
    tmp.append(i)
    pos.append(tmp)

pos.sort()
x_sort=pos[:]

pos.sort(key=lambda a: a[1])
y_sort=pos[:]

pos.sort(key=lambda a: a[2])
z_sort=pos[:]

uf=[i for i in range(n)]
heap=[]
for i in range(n-1):
    heapq.heappush(heap, (abs(x_sort[i][0]-x_sort[i+1][0]), x_sort[i][-1], x_sort[i+1][-1]))
    heapq.heappush(heap, (abs(y_sort[i][1]-y_sort[i+1][1]), y_sort[i][-1], y_sort[i+1][-1]))
    heapq.heappush(heap, (abs(z_sort[i][2]-z_sort[i+1][2]), z_sort[i][-1], z_sort[i+1][-1]))

ans=0
while heap:
    cost, a, b=heapq.heappop(heap)
    if find(a)==find(b):
        continue
    else:
        union(a, b)
        ans+=cost
print(ans)

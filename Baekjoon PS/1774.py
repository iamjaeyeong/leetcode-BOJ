import sys, heapq
input=sys.stdin.readline

def find(a):
    if a==uf[a]:
        return a
    else:
        uf[a]=find(uf[a])
        return uf[a]

def union(a, b):
    a=find(a)
    b=find(b)
    uf[a]=uf[b]

def distance(pos1, pos2):
    return pow(pow(pos1[0]-pos2[0],2)+pow(pos1[1]-pos2[1], 2), 1/2)

n, m=map(int, input().split())
uf=[i for i in range(n)]
pos=[]
for i in range(n):
    pos.append(list(map(int, input().split())))
connection=[]
for i in range(m):
    connection.append(list(map(lambda x : int(x)-1, input().split())))

heap=[]
for i in range(len(pos)):
    for j in range(i+1,len(pos)):
        heapq.heappush(heap, (distance(pos[i], pos[j]), i, j))

ans=0

for i, j in connection:
    union(i, j)


while heap:
    dis, i, j=heapq.heappop(heap)
    if find(i)==find(j):
        continue
    else:
        ans+=dis
        union(i, j)
print("%0.2f" %ans)

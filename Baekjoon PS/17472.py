import sys, heapq
input=sys.stdin.readline

def island(map, pos, name):
    if pos[0]>0 and map[pos[0]-1][pos[1]]==1:
        map[pos[0]-1][pos[1]]=name
        island(map, [pos[0]-1, pos[1]], name)

    if pos[0]<len(map)-1 and map[pos[0]+1][pos[1]]==1:
        map[pos[0]+1][pos[1]]=name
        island(map, [pos[0]+1, pos[1]], name)

    if pos[1]>0 and map[pos[0]][pos[1]-1]==1:
        map[pos[0]][pos[1]-1]=name
        island(map, [pos[0], pos[1]-1], name)

    if pos[1]<len(map[0])-1 and map[pos[0]][pos[1]+1]==1:
        map[pos[0]][pos[1]+1]=name
        island(map, [pos[0], pos[1]+1], name)

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


n, m=map(int, input().split())

country=[]
for i in range(n):
    country.append(list(map(int, input().split())))

name=2
for i in range(n):
    for j in range(m):
        if country[i][j]==1:
            country[i][j]=name
            island(country, [i, j], name)
            name+=1

heap=[]
uf=[i for i in range(name-2)]
for i in range(n):
    tmp=-1
    bridge=0
    for j in range(m):
        if country[i][j]!=0:
            if tmp==-1:
                tmp=country[i][j]
            elif tmp==country[i][j]:
                bridge=0
                continue
            else:
                if bridge>1:
                    heapq.heappush(heap,(bridge, tmp, country[i][j]))
                bridge=0
                tmp=country[i][j]
        else:
            if tmp!=-1:
                bridge+=1

for j in range(m):
    tmp=-1
    bridge=0
    for i in range(n):
        if country[i][j]!=0:
            if tmp==-1:
                tmp=country[i][j]
            elif tmp==country[i][j]:
                bridge=0
                continue
            else:
                if bridge>1:
                    heapq.heappush(heap,(bridge, tmp, country[i][j]))
                bridge=0
                tmp=country[i][j]
        else:
            if tmp!=-1:
                bridge+=1    

ans=0
while heap:
    dis, s, e=heapq.heappop(heap)
    s=s-2
    e=e-2
    if find(s)==find(e):
        continue
    else:
        union(s, e)
        ans+=dis
fail=0
std=find(uf[0])
for i in uf:
    if find(i)!=std:
        fail=1
        break

if fail:
    print(-1)
else:
    print(ans)


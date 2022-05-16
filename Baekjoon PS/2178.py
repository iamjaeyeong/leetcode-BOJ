import sys
input=sys.stdin.readline
from collections import deque
n, m=map(int, input().split())

map=[]
for i in range(n):
    a=input().rstrip()
    map.append([int(i) for i in a])

route=deque()
route.append(deque())
route.append(deque())
route[0].append([0,0])
cnt=1
tmp=[]
temp=0
while(1):
    if len(route[0])==0:
        route.append(deque())
        route.popleft()
        cnt+=1
    pos=route[0].popleft()
    map[pos[0]][pos[1]]=-1
    if pos==[n-1, m-1]:
        break
    if pos[0]>0 and map[pos[0]-1][pos[1]]>0:
        map[pos[0]-1][pos[1]]=-1
        route[1].append([pos[0]-1,pos[1]])
    if pos[1]>0 and map[pos[0]][pos[1]-1]>0:
        map[pos[0]][pos[1]-1]=-1
        route[1].append([pos[0],pos[1]-1])
    if pos[0]<n-1 and map[pos[0]+1][pos[1]]>0:
        map[pos[0]+1][pos[1]]=-1
        route[1].append([pos[0]+1,pos[1]])
    if pos[1]<m-1 and map[pos[0]][pos[1]+1]>0:
        map[pos[0]][pos[1]+1]=-1
        route[1].append([pos[0],pos[1]+1])

print(cnt)

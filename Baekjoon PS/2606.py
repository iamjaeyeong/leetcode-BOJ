import sys
input=sys.stdin.readline
from collections import deque

computers=int(input())
connected=int(input())
connection=[]
for i in range(connected):
    connection.append(list(map(int, input().split())))
connections={i:[] for i in range(1,computers+1)}
for i in connection:
    connections[i[0]].append(i[1])
for i in connection:
    connections[i[1]].append(i[0])
for i in connections:
    connections[i].sort()

path=[0 for i in range(101)]
deq=deque()
deq.append(1)
path[1]=1
bfs=[]
while(1):
    if len(deq)==0:
        break
    else:
        bfs.append(deq.popleft())
        for i in connections[bfs[-1]]:
            if path[i]==1:
                continue
            else:
                path[i]=1
                deq.append(i)
print(len(bfs)-1)

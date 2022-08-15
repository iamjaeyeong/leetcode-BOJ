import sys
from collections import deque
input = sys.stdin.readline

singer, pd = list(map(int, input().split()))

orders = []
for i in range(pd):
    orders.append(list(map(int, input().split()))[1:])
    
answer = []
topo_sort = [0 for i in range(singer)]
visits = []
edges = {i:[] for i in range(singer)}

for order in orders:
    for i in range(1, len(order)):
        topo_sort[order[i]-1] += 1
        edges[order[i-1]-1].append(order[i]-1)
        
for i in range(len(topo_sort)):
    if topo_sort[i]==0:
        visits.append(i)
while visits:
    next_visit = []
    for visit in visits:
        answer.append(visit+1)
        topo_sort[visit] = -1
        for vertex in edges[visit]:
            topo_sort[vertex] -= 1        
    for i in range(len(topo_sort)):
        if topo_sort[i]==0:
            next_visit.append(i)
    visits = next_visit

if len(answer)!=singer:
    print(0)
else:
    print(answer)
    
# bellman-ford algorithm
from collections import deque
import sys, math
input=sys.stdin.readline
inf=math.inf
n, m=map(int, input().split())
bus=[]
for i in range(m):
    bus.append(list(map(int, input().split())))

ans=[inf for i in range(n+1)]
ans[1]=0

bus_dict={i:[] for i in range(1, n+1)}
for i in bus:
    bus_dict[i[0]].append([i[1], i[2]])

for _ in range(n):
    for i in bus_dict:
        for j in bus_dict[i]:
            dest=j[0]
            cost=j[1]
            if ans[i]+cost<ans[dest]:
                ans[dest]=ans[i]+cost

circulation=ans[:]

for i in bus_dict:
    for j in bus_dict[i]:
        dest=j[0]
        cost=j[1]
        if ans[i]+cost<ans[dest]:
            ans[dest]=ans[i]+cost

for i in range(n+1):
    if circulation[i]!=ans[i]:
        ans=-1
        break

if ans==-1:
    print(ans)
else:
    for i in range(2, n+1):
        if ans[i]==inf:
            print(-1)
        else:
            print(ans[i])
    

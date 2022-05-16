import sys, heapq
from math import inf
input=sys.stdin.readline

def dijkstra(dep, c):
    finished=[0 for i in range(c+1)]
    route=[None for i in range(c+1)]
    dp=[inf for i in range(c+1)]
    heap=[]
    heapq.heappush(heap, (0, dep))
    dp[dep]=0
    while heap:
        tmp, s=heapq.heappop(heap)
        if finished[s]==1:
            continue
        else:
            finished[s]=1
        for d, cost in edges[s]:
            if dp[d]>dp[s]+cost:
                dp[d]=dp[s]+cost
                heapq.heappush(heap, (dp[d], d))
                route[d]=s
    return dp, route

c=int(input())
e=int(input())
edges=[[] for i in range(c+1)]
for i in range(e):
    dep, des, cos=map(int, input().split())
    edges[dep].append([des, cos])
dep, des= map(int, input().split())
ans, route=dijkstra(dep, c)
print(ans[des])
r=[]
while 1:
    r.append(des)
    if des==dep:
        break
    des=route[des]
r.reverse()
print(len(r))
print(*r)

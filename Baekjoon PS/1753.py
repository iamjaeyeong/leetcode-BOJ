import sys, heapq, math
input=sys.stdin.readline
inf=math.inf

n, m=map(int, input().split())
start=int(input())
edges=[]
edge_dict={i:[] for i in range(1, n+1)}
ans=[inf for i in range(n+1)]
ans[start]=0
for i in range(m):
    edges.append(list(map(int, input().split())))
for i in edges:
    edge_dict[i[0]].append([i[1], i[2]])
heap=[]
heapq.heappush(heap, (0,start))
finish=[0 for i in range(n+1)]
while(1):
    if len(heap)==0:
        break
    cost, start=heapq.heappop(heap)
    if finish[start]==1:
        continue
    else:
        finish[start]=1
    for i in edge_dict[start]:
        tmp=i[1]+cost
        if tmp<ans[i[0]]:
            ans[i[0]]=cost+i[1]
            heapq.heappush(heap, (tmp, i[0]))
for i in range(1, len(ans)):
    if ans[i]==inf:
        print('INF')
    else:
        print(ans[i])
import sys, heapq, math
input=sys.stdin.readline
inf=math.inf
heap=[]
n, m=map(int, input().split())
edge=[]
for i in range(m):
    edge.append(list(map(int, input().split())))
v1, v2=map(int, input().split())
edge_dict={i:[] for i in range(1, n+1)}
for i in edge:
    edge_dict[i[0]].append([i[1], i[2]])
    edge_dict[i[1]].append([i[0], i[2]])

def dijkstra(edge_dict, n, start):
    ans=[inf for i in range(n+1)]
    ans[start]=0
    heap=[]
    heapq.heappush(heap, (0, start))
    while(1):
        if len(heap)==0:
            break
        cost, start=heapq.heappop(heap)
        for i in edge_dict[start]:
            tmp=i[1]+ans[start]
            if tmp<ans[i[0]]:
                ans[i[0]]=tmp
                heapq.heappush(heap, (tmp, i[0]))
    return ans

tmp=dijkstra(edge_dict, n, 1)
_1_to_v1=tmp[v1]
_1_to_v2=tmp[v2]
tmp=dijkstra(edge_dict, n, v1)
_v1_to_v2=tmp[v2]
_v1_to_n=tmp[n]
tmp=dijkstra(edge_dict, n, v2)
_v2_to_v1=tmp[v1]
_v2_to_n=tmp[n]
ans=min(_1_to_v1+_v1_to_v2+_v2_to_n, _1_to_v2+_v2_to_v1+_v1_to_n)
if ans==inf:
    print(-1)
else:
    print(ans)
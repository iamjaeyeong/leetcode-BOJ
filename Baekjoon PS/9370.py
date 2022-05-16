import sys, math, heapq
input=sys.stdin.readline
inf=math.inf
def dijkstra(start):
    ans=[100000000 for i in range(n+1)]
    heap=[]
    ans[start]=0
    heapq.heappush(heap, (0,start))
    while (heap):
        cost, start=heapq.heappop(heap)
        for i in edge_dict[start]:
            tmp=cost+i[1]
            if tmp<ans[i[0]]:
                ans[i[0]]=tmp
                heapq.heappush(heap, (tmp, i[0]))
    return ans

# def dijkstra(start):
#     heap = []
#     heapq.heappush(heap, [0, start])
#     dp = [100000000 for i in range(n + 1)]
#     dp[start] = 0
#     while heap:
#         we, nu = heapq.heappop(heap)
#         for ne, nw in edge_dict[nu]:
#             wei = we + nw
#             if dp[ne] > wei:
#                 dp[ne] = wei
#                 heapq.heappush(heap, [wei, ne])
#     return dp

case=int(input())
for i in range(case):
    n, m, t=map(int, input().split())
    s, g, h=map(int, input().split())
    edges=[]
    for j in range(m):
        edges.append(list(map(int, input().split())))
    target=[]
    for j in range(t):
        target.append(int(input()))
    edge_dict=[[] for i in range(n+1)]
    for j in edges:
        edge_dict[j[0]].append([j[1], j[2]])
        edge_dict[j[1]].append([j[0], j[2]])
    s_to_all=dijkstra(s)
    s_to_g=s_to_all[g]
    s_to_h=s_to_all[h]
    for j in edge_dict[h]:
        if j[0]==g:
            g_to_h=h_to_g=j[1]
            break
    g_to_all=dijkstra(g)
    h_to_all=dijkstra(h)
    ans=[]
    for j in target:
        if s_to_all[j]==s_to_g+g_to_h+h_to_all[j] or s_to_all[j]==s_to_h+h_to_g+g_to_all[j]:
            ans.append(j)
    ans.sort()
    print(*ans)
    


    


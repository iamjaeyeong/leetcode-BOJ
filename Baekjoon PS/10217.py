import sys, math, heapq
input=sys.stdin.readline
inf=math.inf
# ap_dict - destination, cost, time
def dijkstra(ap_dict, n, m):
    dp=[[inf for j in range(n+1)] for i in range(m+1)]
    # dp[i][j] = i money, j airport -> time
    dp[0][1]=0
    for money, i in enumerate(dp):
        for airport, j in enumerate(i):
            if j==inf:
                continue
            else:
                for k in ap_dict[airport]:
                    if money+k[1]>m:
                        continue
                    else:
                        if dp[money+k[1]][k[0]]>k[2]+j:
                            dp[money+k[1]][k[0]]=k[2]+j
    ans=inf
    for i in range(1,m+1):
        if ans>dp[i][n]:
            ans=dp[i][n]
    return ans


t=int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    ap=[]
    for i in range(k):
        ap.append(list(map(int, input().split())))
    ap_dict={i:[] for i in range(1, n+1)}
    for i in ap:
        ap_dict[i[0]].append([i[1], i[2], i[3]])
    ans=dijkstra(ap_dict, n, m)
    if ans==inf:
        print('Poor KCM')
    else:
        print(ans)




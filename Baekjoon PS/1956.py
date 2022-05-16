# floyd-warshall algorithm
import sys, math
input=sys.stdin.readline
inf=math.inf
v, e=map(int, input().split())
edges=[[] for i in range(v+1)]
cycle=[[] for i in range(v+1)]
for i in range(e):
    a, b, c=map(int, input().split())
    edges[a].append([b,c])
    # start, destination, distance
    cycle[b].append([a,c])
dp=[[inf]*(v+1) for i in range(v+1)]
# dp[i][j] -> i to j distance

for i in range(v+1):
    dp[i][i]=0

for i in range(1, v+1):
    for j in edges[i]:
        dp[i][j[0]]=j[1]

for i in range(1, v+1):
    # if you pass by vertex i,
    for j in range(1, v+1):
        if j==i:
            continue
        for k in range(1, v+1):
            # vertex j to k
            if k==i or j==k:
                continue
            if dp[j][k]>dp[j][i]+dp[i][k]:
                dp[j][k]=dp[j][i]+dp[i][k]

ans=inf
for i in range(1, v+1):
    for j in cycle[i]:
        if ans>dp[i][j[0]]+dp[j[0]][i]:
            ans=dp[i][j[0]]+dp[j[0]][i]
if ans==inf:
    print(-1)
else:
    print(ans)



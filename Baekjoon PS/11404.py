# floyd-warshall algorithm
import sys, math
input=sys.stdin.readline
inf=math.inf

n=int(input())
m=int(input())
bus=[]
for i in range(m):
    bus.append(list(map(int, input().split())))
dp=[[inf for i in range(n+1)]for i in range(n+1)]
# i에서 j로 가는 cost
for i in range(n):
    dp[i][i]=0

for i in bus:
    if dp[i[0]][i[1]]>i[2]:
        dp[i[0]][i[1]]=i[2]


for p in range(1, n+1):
    for i in range(1, n+1):
        if i==p:
            continue
        for j in range(1, n+1):
            if i==j or j==p:
                continue
            if dp[i][j]>dp[i][p]+dp[p][j]:
                dp[i][j]=dp[i][p]+dp[p][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if dp[i][j]==inf:
            print(0, end=' ')
        else:
            print(dp[i][j], end=' ')
    if i!=n:
        print()
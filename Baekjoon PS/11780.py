# floyd-warshall
import sys
from collections import deque
from math import inf
input=sys.stdin.readline

def dfs(dep, des, ret):
    if dp[dep][des]==None:
        ret.append(dep)
    else:
        dfs(dep, dp[dep][des], ret)
        dfs(dp[dep][des], des, ret)

c=int(input())
b=int(input())
edges=[[] for i in range(c+1)]
dp=[[None for i in range(c+1)] for j in range(c+1)]
for i in range(b):
    dep, des, cos=map(int, input().split())
    edges[dep].append([des, cos])
floyd=[[inf for i in range(c+1)] for j in range(c+1)]
for i in range(c+1):
    floyd[i][i]=0
    for d, cost in edges[i]:
        if floyd[i][d]>cost:
            floyd[i][d]=cost
for i in range(1,c+1):
    for j in range(1, c+1):
        for k in range(1, c+1):
            if i==k or j==i or j==k:
                continue
            else:
                if floyd[j][k]>floyd[j][i]+floyd[i][k]:
                    floyd[j][k]=floyd[j][i]+floyd[i][k]
                    dp[j][k]=i
for i in range(1,c+1):
    for j in range(1, c+1):
        if floyd[i][j]==inf:
            floyd[i][j]=0
for i in floyd[1:]:
    print(*i[1:])
for i in range(1, c+1):
    for j in range(1, c+1):
        if floyd[i][j]==0:
            print(0)
        else:
            route=[]
            dfs(i, j, route)
            route.append(j)
            print(len(route), end=' ')
            print(*route)



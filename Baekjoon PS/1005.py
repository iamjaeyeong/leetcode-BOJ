import sys
from collections import deque
input=sys.stdin.readline

t=int(input())

def dfs(edges, cost, node, dp):
    mx=0
    for i in edges[node]:
        if dp[i]==-1:
            tmp=dfs(edges, cost, i, dp)
            if tmp>mx:
                mx=tmp
            dp[i]=tmp
        else:
            if mx<dp[i]:
                mx=dp[i]
    return mx+cost[node-1]

def test_case():
    n, k=map(int, input().split())
    cost=list(map(int, input().split()))
    edges={i:[] for i in range(n+1)}
    for i in range(k):
        a, b=map(int, input().split())
        edges[b].append(a)
    dp=[-1 for i in range(n+1)]
    target=int(input())
    return dfs(edges,cost, target, dp)
    
for i in range(t):
    print(test_case())


    
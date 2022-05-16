import sys
input=sys.stdin.readline
from math import inf

def func(node, prev, prev_prev):
    if prev==None:
        for i in edges[node]:
            func(i, node, None)
    elif prev_prev==None:
        c[prev][0].append(node)
        for i in edges[node]:
            if i!=prev:
                func(i, node, prev)
    else:
        c[prev_prev][1].append(node)
        c[prev][0].append(node)
        for i in edges[node]:
            if i!=prev:
                func(i, node, prev)

def dfs(pre, node):
    for i in edges[node]:
        if i==pre:
            continue
        else:
            dfs(node, i)

    if c[node][0]==[]:
        dp[node]=vertex[node]
        ans[node]=0
    elif c[node][1]==[]:
        sm=0
        for i in c[node][0]:
            sm+=dp[i]
        if vertex[node]>sm:
            dp[node]=vertex[node]
            ans[node]=0
        else:
            dp[node]=sm
            ans[node]=1
    else:
        sm=0
        for i in c[node][0]:
            sm+=dp[i]
        sm2=0
        for i in c[node][1]:
            sm2+=dp[i]
        if vertex[node]+sm2>sm:
            dp[node]=vertex[node]+sm2
            ans[node]=0
        else:
            dp[node]=sm
            ans[node]=1

def backtracking(pre, node, tmp):
    if tmp==1:
        if ans[node]==0:
            ret.append(node+1)
            tmp=0
        for i in edges[node]:
            if i!=pre:
                backtracking(node, i, tmp)
    else:
        for i in edges[node]:
            if i!=pre:
                backtracking(node, i, 1)
    
n=int(input())
vertex=list(map(int, input().split()))
edges={i:[] for i in range(n)}
for i in range(n-1):
    a, b=map(lambda x: int(x)-1, input().split())
    edges[a].append(b)
    edges[b].append(a)
dp=[0 for i in range(n)]
ans=[-1 for i in range(n)]
c=[[[], []] for i in range(n)]
ret=[]
func(0, None, None)
dfs(None, 0)
print(dp[0])
backtracking(None, 0, 1)
ret.sort()
print(*ret)
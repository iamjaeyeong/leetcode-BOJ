import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(cnt, prev, node):
    leaf=0
    for i in edges[node]:
        if i==prev:
            continue
        else:
            if dfs(cnt, node, i)==0:
                leaf=1
    if leaf:
        cnt[0]+=1
        return 1
    else:
        return 0


n=int(input())
edges={i:[] for i in range(n)}
for i in range(n-1):
    a ,b=map(lambda x: int(x)-1, input().split())
    edges[a].append(b)
    edges[b].append(a)
ans=[0]
dfs(ans, -1, 0)
print(ans[0])

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

def query(edge, node, root):
    for i in edge[node]:
        if i==root:
            continue
        else:
            dp[node]+=query(edge, i, node)
    return dp[node]


        

n, r, q=map(int, input().split())

edge=[]
for i in range(n-1):
    edge.append(list(map(int, input().split())))

edges={i:[] for i in range(n+1)}
for i in edge:
    edges[i[0]].append(i[1])
    edges[i[1]].append(i[0])

dp=[1 for i in range(n+1)]
query(edges, r, -1)

ans=[]
for i in range(q):
    ans.append(int(input()))
for i in ans:
    print(dp[i])
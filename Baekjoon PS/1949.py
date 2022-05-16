import sys
input=sys.stdin.readline

def dfs(ans, prev, node, superior):
    is_imperior=superior
    if superior:
        ans[0]+=citizen[node]
        print(node)
    for i in edges[node]:
        if i==prev:
            continue
        else:
            if is_imperior:
                dfs(ans, node, i, 0)
            else:
                dfs(ans, node, i, 1)

n=int(input())
citizen=list(map(int, input().split()))
edges={i:[] for i in range(n)}
for i in range(n-1):
    a, b=map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)
ans=[0]
dfs(ans, None, 1, 0)
ans_1=ans[0]
ans=[0]
print()
dfs(ans, None, 1, 1)
ans_2=ans[0]
print(ans_1, ans_2)

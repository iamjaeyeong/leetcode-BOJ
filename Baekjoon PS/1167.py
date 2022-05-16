import sys
from collections import deque
input=sys.stdin.readline

def dfs(start, l, edges, last):
    mx=l
    node=start
    for i in edges[start]:
        if i[0]!=last:
            a, n=dfs(i[0], l+i[1], edges, start)
            if mx<a:
                mx=a
                node=n
    return mx, node



v=int(input())
edges=[[] for i in range(v+1)]
leaf=[]
for i in range(v):
    tmp=list(map(int, input().split()))
    idx=tmp[0]
    for j in range(1, len(tmp)-1, 2):
        edges[idx].append([tmp[j], tmp[j+1]])
    if len(tmp)==4:
        leaf.append(idx)
mx, node=dfs(leaf[0], 0, edges, None)
ans_mx, ans_node=dfs(node, 0, edges, None)
print(ans_mx)
        




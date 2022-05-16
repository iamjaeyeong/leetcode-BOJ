import sys
input=sys.stdin.readline

def dfs(map, idx, ans, group):
    if map[idx[0]][idx[1]]>0:
        map[idx[0]][idx[1]]=(-1)*group
        ans[-1]+=1
        if idx[0]>0:
            dfs(map, [idx[0]-1, idx[1]], ans, group)
        if idx[1]>0:
            dfs(map, [idx[0], idx[1]-1], ans, group)
        if idx[0]<len(map)-1:
            dfs(map, [idx[0]+1, idx[1]], ans, group)
        if idx[1]<len(map)-1:
            dfs(map, [idx[0], idx[1]+1], ans, group)
n=int(input())
map=[]
for i in range(n):
    a=input().rstrip()
    map.append([int(i) for i in a])
ans=[]
tmp=1

for i in range(n):
    for j in range(n):
        if map[i][j]>0:
            ans.append(0)
            dfs(map, [i,j], ans, tmp)
            tmp+=1



print(len(ans))
ans.sort()
for i in ans:
    print(i)



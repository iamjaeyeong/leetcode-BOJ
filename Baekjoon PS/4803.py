import sys
input=sys.stdin.readline

def dfs(start, last):
    tmp=1
    for i in edges[start]:
        if i==last:
            continue
        elif finished[i]==1:
            tmp=0
        elif tmp:
            finished[i]=1
            tmp=dfs(i, start)
        else:
            finished[i]=1
            dfs(i, start)
    if tmp==0:
        return 0
    else:
        return 1
c=1
while 1:
    a, b=map(int, input().split())
    if a==b==0:
        break
    edges=[[] for i in range(a+1)]
    for i in range(b):
        m, n=map(int, input().split())
        edges[m].append(n)
        edges[n].append(m)
    cnt=0
    finished=[0 for i in range(a+1)]
    for i in range(1, a+1):
        if finished[i]==1:
            continue
        else:
            finished[i]=1
            cnt+=dfs(i, -1)
    if cnt==0:
        print(f'Case {c}: No trees.')
    elif cnt==1:
        print(f'Case {c}: There is one tree.')
    else:
        print(f'Case {c}: A forest of {cnt} trees.')
    c+=1


import sys
input=sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    n, m=map(int ,input().split())
    lines=[]
    path=[-1 for i in range(n+1)]
    for j in range(m):
        lines.append(list(map(int, input().split())))
    dic={i:[] for i in range(1, n+1)}
    for i in lines:
        dic[i[0]].append(i[1])
        dic[i[1]].append(i[0])
    for i in range(1, len(path)):
        if path[i]==-1:
            stop=0
            yes=0
            deq=deque()
            deq.append(i)
            path[i]=0
            while(1):
                if len(deq)==0:
                    yes=1
                    break
                node=deq.popleft()
                tmp=path[node]
                for j in dic[node]:
                    if path[j]==-1:
                        path[j]=(tmp+1)%2
                        deq.append(j)
                    elif path[j]==tmp:
                        stop=1
                        yes=0
                        break
                if stop:
                    break
            if stop:
                break
    if yes:
        print('YES')
    else:
        print('NO')

    
    
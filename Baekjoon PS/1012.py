import sys
input=sys.stdin.readline

def group(field, pos):
    if field[pos[0]][pos[1]]>0:
        field[pos[0]][pos[1]]*=(-1)
        if pos[0]>0:
            group(field, [pos[0]-1, pos[1]])
        if pos[1]>0:
            group(field, [pos[0], pos[1]-1])
        if pos[0]<len(field)-1:
            group(field, [pos[0]+1, pos[1]])
        if pos[1]<len(field[0])-1:
            group(field, [pos[0], pos[1]+1])

case=int(input())
for _ in range(case):
    m, n, cabbage=map(int, input().split())
    field=[[0 for i in range(m)] for i in range(n)]
    ans=0
    for i in range(cabbage):
        pos=list(map(int, input().split()))
        field[pos[1]][pos[0]]=1
    for i in range(n):
        for j in range(m):
            if field[i][j]>0:
                ans+=1
                group(field, [i,j])
                # for a in field:
                #     print(*a)
                # print('==========')
    print(ans)
    
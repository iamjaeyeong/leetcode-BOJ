import sys, math
input=sys.stdin.readline

n=int(input())
fluid=list(map(int, input().split()))
fluid.sort()

idx=None
tmp=math.inf
for i in range(len(fluid)):
    p1, p2=0, len(fluid)-1
    while 1:
        if p1==p2:
            break
        if p1==i:
            p1+=1
        elif p2==i:
            p2-=1
        else:
            s=fluid[p1]+fluid[p2]+fluid[i]
            if abs(tmp)>abs(s):
                tmp=s
                idx=[p1, p2, i]
            if s>0:
                p2-=1
            else:
                p1+=1
ans=list(map(lambda x: fluid[x], idx))
ans.sort()
print(*ans)
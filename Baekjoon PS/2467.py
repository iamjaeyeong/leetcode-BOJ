import sys
input=sys.stdin.readline
from math import inf

n=int(input())
fluid=list(map(int, input().split()))
fluid.sort()
p1, p2=0, n-1

mn=inf
ans=[None, None]

while 1:
    if p1==p2 or mn==0:
        break
    if mn>abs(fluid[p1]+fluid[p2]):
        mn=abs(fluid[p1]+fluid[p2])
        ans=[p1, p2]
    if fluid[p1]+fluid[p2]<0:
        p1+=1
    else:
        p2-=1
print(fluid[ans[0]], fluid[ans[1]])



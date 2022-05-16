import sys, math
input=sys.stdin.readline

def area(pos):
    tmp=pos[-1][0]*pos[0][1]
    for i in range(len(pos)-1):
        tmp+=pos[i][0]*pos[i+1][1]
    tmp2=pos[-1][1]*pos[0][0]
    for i in range(len(pos)-1):
        tmp2+=pos[i][1]*pos[i+1][0]
    return abs(tmp-tmp2)/2

n=int(input())
pos=[]
for i in range(n):
    pos.append(list(map(int, input().split())))
ans=area(pos)
print("%0.1f" %ans)


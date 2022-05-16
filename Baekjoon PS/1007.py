import sys
import math
input=sys.stdin.readline

n=int(input())

def backtracking(n, k, tmp, ap, ret):
    if tmp==0:
        ret.append(ap)
    else:
        for i in range(k, n-tmp+1):
            backtracking(n, i+1, tmp-1, ap+[i], ret)

def distance(pos1, pos2):
    return pow(pow(pos1[0]-pos2[0], 2)+pow(pos1[1]-pos2[1], 2), 1/2)

def main():
    dots=int(input())
    pos=[]
    x_sum=0
    y_sum=0
    for i in range(dots):
        tmp=list(map(int, input().split()))
        x_sum+=tmp[0]
        y_sum+=tmp[1]
        pos.append(tmp)
    bf=[]
    backtracking(dots, 0, dots//2, [], bf)
    l=len(bf)//2
    dis=math.inf
    for i in range(l+1):
        pos1_x=sum(pos[j][0] for j in bf[i])
        pos1_y=sum(pos[j][1] for j in bf[i])
        pos2_x=x_sum-pos1_x
        pos2_y=y_sum-pos1_y
        d=distance([pos1_x, pos1_y], [pos2_x, pos2_y])
        if dis>d:
            dis=d
    return dis
for i in range(n):
    ans=main() 
    print("%0.10f" %ans)
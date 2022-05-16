# memory limit exceed
import sys
input=sys.stdin.readline
from math import inf

def distance(case, pos):
    ret=abs(case[0]-pos[0])
    ret+=abs(case[1]-pos[1])
    return ret

n=int(input())
# size of city
w=int(input())
# number of cases
cases=[]
ans=[]
for i in range(w):
    cases.append(list(map(lambda x: int(x)-1, input().split())))
pol1=[0 ,0]
pol2=[n-1, n-1]
dp=[[inf for i in range(w+1)] for j in range(w+1)]
dp_pol=[[None for j in range(w+1) ] for i in range(w+1)]
dp[0][1]=distance(cases[0], pol2)
# 2번 경찰차가 갔을 때
dp[1][0]=distance(cases[0], pol1)
# 1번 경찰차가 갔을 때
for i in range(1,w):
    for j in range(i+1):
        if dp[j][i+1]>dp[j][i]+distance(cases[i], cases[i-1]):
            dp[j][i+1]=dp[j][i]+distance(cases[i], cases[i-1])
            dp_pol[j][i+1]=[j, i]
        if j==0:
            if dp[i+1][i]>dp[j][i]+distance(cases[i], pol1):
                dp[i+1][i]=dp[j][i]+distance(cases[i], pol1)
                dp_pol[i+1][i]=[j, i]
        else:
            if dp[i+1][i]>dp[j][i]+distance(cases[i], cases[j-1]):
                dp[i+1][i]=dp[j][i]+distance(cases[i], cases[j-1])
                dp_pol[i+1][i]=[j, i]
    for j in range(i+1):
        if dp[i+1][j]>dp[i][j]+distance(cases[i], cases[i-1]):
            dp[i+1][j]=dp[i][j]+distance(cases[i], cases[i-1])
            dp_pol[i+1][j]=[i, j]
        if j==0:
            if dp[i][i+1]>dp[i][j]+distance(cases[i], pol2):
                dp[i][i+1]=dp[i][j]+distance(cases[i], pol2)
                dp_pol[i][i+1]=[i, j]
        else:
            if dp[i][i+1]>dp[i][j]+distance(cases[i], cases[j-1]):
                dp[i][i+1]=dp[i][j]+distance(cases[i], cases[j-1])
                dp_pol[i][i+1]=[i, j]

dis=inf
for i in range(w):
    if dis>dp[w][i]:
        dis=dp[w][i]
        idx=[w, i]
    if dis>dp[i][w]:
        dis=dp[i][w]
        idx=[i, w]

for i in range(w, 0, -1):
    if idx[0]==i:
        ans.append(1)
    else:
        ans.append(2)
    idx=dp_pol[idx[0]][idx[1]]
ans.reverse()
print(dis)
for i in ans:
    print(i)
    

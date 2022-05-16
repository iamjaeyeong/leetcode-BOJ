import sys, math
input=sys.stdin.readline
from itertools import accumulate as acc
inf=math.inf
def make_sum_lst(lst):
    ret=[[0 for j in range(len(lst))] for i in range(len(lst))]
    ret[0][0]=lst[0]
    for i in range(1, len(lst)):
        for j in range(i+1):
            ret[j][i]=ret[j][i-1]+lst[i]
    return ret

n=int(input())
for i in range(n):
    m=int(input())
    chapter=list(map(int, input().split()))
    sum_lst=make_sum_lst(chapter)
    dp=[[0 for j in range(m)]for k in range(m)]
    dp[0][0]=chapter[0]
    dp[0][1]=chapter[0]+chapter[1]
    dp[1][1]=chapter[1]
    for p in range(2, m):
        dp[p][p]=chapter[p]
        for q in range(p-1, -1, -1):
            tmp=inf
            for t in range(p-q):
                if t!=0 and t!=p-q-1:
                    if tmp>dp[q][q+t] + dp[q+t+1][p] + sum_lst[q][p]:
                        tmp=dp[q][q+t] + dp[q+t+1][p] + sum_lst[q][p]
                elif t!=0:
                    if tmp > dp[q][q+t] + sum_lst[q][p]:
                        tmp=dp[q][q+t] + sum_lst[q][p]
                elif t!=p-q-1:
                    if tmp>sum_lst[q][p] + dp[q+t+1][p]:
                        tmp=sum_lst[q][p] + dp[q+t+1][p]
                else:
                    if tmp>sum_lst[q][p]:
                        tmp=sum_lst[q][p]
            dp[q][p]=tmp
    print(dp[0][-1])
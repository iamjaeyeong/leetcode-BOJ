
import sys, math
input=sys.stdin.readline
inf= math.inf
from itertools import accumulate as acc


n=int(input())
for i in range(n):
    m=int(input())
    chapter=list(map(int, input().split()))
    sum_lst=[]
    for p in range(0, m):
        sum_lst.append(list(acc(chapter[i] for i in range(p, len(chapter)))))
    dp=[[0 for j in range(m)]for k in range(m)]
    c_new=[]
    for j in range(m):
        c=c_new
        c_new=[]
        for k in range(m-j):
            tmp=inf
            idx=-1
            if j==0:
                dp[k][j+k]=chapter[k]
            elif j==1:
                dp[k][j+k]=dp[k][j+k-1]+dp[k+1][j+k]
                c_new.append(k)
            else:   
                for l in range(c[k], c[k+1]+1):
                    if l==k:
                        a=dp[l+1][j+k]+sum_lst[k][j]
                        if tmp > a:
                            tmp=a
                            idx=l
                    elif l==j+k-1:
                        a=dp[k][l]+sum_lst[k][j]
                        if tmp > a:
                            tmp=a
                            idx=l                        
                    else:
                        a=dp[k][l]+dp[l+1][j+k]+sum_lst[k][j]
                        if tmp > a:
                            tmp=a
                            idx=l
                dp[k][j+k]=tmp
                c_new.append(idx)
    print(dp[0][-1])


import sys, math
input=sys.stdin.readline

n=int(input())

mat=[]
for i in range(n):
    mat.append(list(map(int, input().split())))

dp=[[0 for i in range(len(mat))] for j in range(len(mat))]
for i in range(1, len(mat)):
    for j in range(len(mat)-i):
        tmp=math.inf
        if i==1:
            dp[j][i+j]=mat[i+j][0]*mat[i+j][1]*mat[j][0]
        else:
            for k in range(j, i+j):
                if k==j:
                    a=dp[k+1][i+j]+mat[j][0]*mat[i+j][1]*mat[j][1]
                    if tmp>a:
                        tmp=a
                        idx=k
                elif k==i+j-1:
                    a=dp[j][k]+mat[j][0]*mat[i+j][1]*mat[k][1]
                    if tmp>a:
                        tmp=a
                        idx=k
                else:
                    a=dp[j][k]+dp[k+1][i+j]+mat[j][0]*mat[k][1]*mat[i+j][1]
                    if tmp>a:
                        tmp=a
                        idx=k
            dp[j][i+j]=tmp
print(dp[0][-1])
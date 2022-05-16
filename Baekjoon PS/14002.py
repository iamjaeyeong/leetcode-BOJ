import sys, math
input=sys.stdin.readline
inf=math.inf
from bisect import bisect_left

n=int(input())
lst=list(map(int, input().split()))
dp=[[]for i in range(n+1)]
tmp=[lst[0]]
dp[1].append([lst[0], 0])
# dp[i] = 길이가 i인 수열
for i in range(1, n):
    idx=bisect_left(tmp, lst[i])
    if idx>len(tmp)-1:
        tmp.append(lst[i])
    else:
        tmp[idx]=lst[i]
    idx+=1
    dp[idx].append([lst[i],i])
for i in dp:
    i.append([0, inf])

print(len(tmp))
ans=[dp[len(tmp)][-2][0]]
tmp2=dp[len(tmp)][-2][1]
for i in range(len(tmp)-1, 0, -1):
    for j in range(len(dp[i])):
        if dp[i][j][1]>tmp2:
            ans.append(dp[i][j-1][0])
            tmp2=dp[i][j-1][1]
            break
ans.reverse()
print(*ans)

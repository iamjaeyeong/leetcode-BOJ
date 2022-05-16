import sys
input=sys.stdin.readline

n, m=map(int, input().split())
dp=[[1]]
for i in range(1, 101):
    cnt=[1]
    for j in range(1, i):
        cnt.append(dp[i-1][j]+dp[i-1][j-1])
    cnt.append(1)
    dp.append(cnt)

print(dp[n][m])


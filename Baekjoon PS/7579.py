import sys
input=sys.stdin.readline

n, need=map(int, input().split())
memory=list(map(int, input().split()))
cost=list(map(int, input().split()))

afford=sum(memory)-need
total=sum(cost)
dp=[[] for i in range(n)]

if memory[0]<=afford:   
    for i in range(cost[0]+1):
        dp[0].append(memory[0])
else:
    dp[0]=[0]

for i in range(1, n):
    dp[i].append(0)
    last=len(dp[i-1])
    for j in range(1,total+1):
        if j<=cost[i]:
            if last>j:
                dp[i].append(min(memory[i], dp[i-1][j]))
            else:
                dp[i].append(memory[i])
        else:
            if last>j:
                dp[i].append(min(memory[i]+dp[i-1][j-cost[i]], dp[i-1][j]))
            elif last>j-cost[i]:
                dp[i].append(memory[i]+dp[i-1][j-cost[i]])
            else:
                break
        if dp[i][-1]>afford:
            del dp[i][-1]
            break

print(total-len(dp[-1])+1)

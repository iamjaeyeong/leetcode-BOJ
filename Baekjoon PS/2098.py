import sys
import math
input = sys.stdin.readline
inf = math.inf

n = int(input())
edges = {i:{} for i in range(n)}

for i in range(n):
    connection = list(map(int, input().split()))
    for j in range(n):
        if connection[j]==0:
            continue
        else:
            edges[i][j] = connection[j]

def constant_digit(s, n):
    len_s = len(s)
    return (n-len_s)*'0' + s

bitMasking = [constant_digit(bin(i)[2:], n) for i in range(pow(2, n))]
power = [pow(2, i) for i in range(n+1)]
dp = [[inf for i in range(pow(2, n))] for j in range(n)]
dp[0][0] = 0

def bfs(visits, n, cnt=[]):
    next_visits = set()
    for visit, visited in visits:
        if visited==power[n]-1:
            continue
        # elif visit==0 and visited!=power[n]-2:
            # continue
        for edge, cost in edges[visit].items():
            if bitMasking[visited][n-edge-1]=='1':
                continue
            elif edge==0 and visited!=power[n]-2:  
                continue  
            next_visited = visited + power[edge]
            if dp[edge][next_visited]>dp[visit][visited]+cost:
                dp[edge][next_visited] = dp[visit][visited] + cost
                next_visits.add((edge, next_visited))
    if next_visits:
        bfs(next_visits, n)
bfs([[0, 0]], n)

print(dp[0][-1])

# bfs로 구현
# 


import sys
input=sys.stdin.readline
n=int(input())
weights=list(map(int, input().split()))
m=int(input())
marbles=list(map(int, input().split()))

dp={weights[0]}
for i in range(1, len(weights)):
    tmp=dp.copy()
    for j in tmp:
        dp.add(j+weights[i])
        dp.add(abs(j-weights[i]))
        dp.add(weights[i])

ans=[]
for marble in marbles:
    if marble in dp:
        ans.append('Y')
    else:
        ans.append('N')
print(*ans)


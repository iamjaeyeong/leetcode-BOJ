import sys
input=sys.stdin.readline

# 먼저 진실을 아는 사람이 들어오는 party를 marking
# 해당 파티에 오는 사람들은 모두 진실을 아는 사람으로 check
# 또 그 사람들이 오는 파티를 모두 진실을 아는 사람으로



n, m=map(int, input().split())
truth=list(map(int, input().split()))
truth=truth[1:]
visitors=[]
party=[]
for i in range(m):
    visitor=list(map(int, input().split()))
    visitors.append(visitor[1:])

tmp=[0 for i in range(50)]
while(1):
    if truth==[]:
        break
    for i in range(len(visitors)):
        if i in party:
            continue
        for j in truth:
            if j in visitors[i]:
                party.append(i)
                for k in visitors[i]:
                    tmp[k-1]=1
                break
    truth=[]
    for i in range(len(tmp)):
        if tmp[i]==1:
            truth.append(i+1)
            tmp[i]=0

print(len(visitors)- len(party))

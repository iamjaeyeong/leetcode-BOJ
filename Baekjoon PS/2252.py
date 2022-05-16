import sys
from collections import deque
input=sys.stdin.readline

n, m=map(int, input().split())
priority=[0 for i in range(n)]
connection=[[] for i in range(n)]

for i in range(m):
    a, b= map(int, input().split())
    connection[a-1].append(b-1)
    priority[b-1]+=1

deq=deque()
ans=[]
while 1:
    stop=1
    for i in range(n):
        if priority[i]==0:
            stop=0
            deq.append(i)
            priority[i]=-1
            for j in connection[i]:
                priority[j]-=1
    if stop:
        break

for i in deq:
    print(i+1, end=' ')


"C:\Users\rlawo\Desktop\공부\python\machine_learning\ch_11-DNN\opt_comparision"
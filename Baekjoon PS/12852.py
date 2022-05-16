import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
dp=[[] for i in range(n+1)]
dp[1]=[1]
queue=deque()
queue.append(1)
while 1:
    pre=queue.popleft()
    if pre+1<n+1 and dp[pre+1]==[]:
        dp[pre+1].append(pre)
        queue.append(pre+1)
    if pre*2<n+1 and dp[pre*2]==[]:
        dp[pre*2].append(pre)
        queue.append(pre*2)
    if pre*3<n+1 and dp[pre*3]==[]:
        dp[pre*3].append(pre)
        queue.append(pre*3)
    if dp[n]!=[]:
        break

cnt=0
tmp=n
idx=dp[n][0]
ans=[]
while 1:
    ans.append(tmp)
    tmp=idx
    idx=dp[idx][0]
    cnt+=1
    if tmp==1:
        if n!=1:
            ans.append(1)
            print(cnt)
        else:
            print(0)
        break
print(*ans)
    


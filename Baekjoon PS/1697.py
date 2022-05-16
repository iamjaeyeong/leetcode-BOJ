import sys
me, sis = map(int, sys.stdin.readline().split())
dp=[0 for i in range(200001)]
pos=[[me],[]]
cnt=0
b=0
while(1):
    for i in pos[0]:
        if i==sis:
            b=1
            break
        else:
            if i*2<len(dp)-1 and dp[i*2]==0:
                dp[i*2]=cnt
                pos[1].append(i*2)
            if i+1<len(dp)-1 and dp[i+1]==0:
                dp[i+1]=cnt
                pos[1].append(i+1)
            if i>0 and dp[i-1]==0:
                dp[i-1]=cnt
                pos[1].append(i-1)
    if b:
        break
    pos[0]=pos[1]
    pos[1]=[]
    cnt+=1
print(cnt)
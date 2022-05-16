n, m=map(int,input().split())
if n>m:
    print(n-m)
    ans=[i for i in range(n, m-1, -1)]
else:
    dp=[100000 for i in range(m*2+1)]
    q=[n]
    dp[n]=0
    bt=[None for i in range(2*m+1)]
    bt[n]=n
    new_q=[]
    cnt=1
    end=0
    while 1:
        while q:
            s=q.pop()
            if s==m:
                end=1
                break
            if s>0:
                if dp[s-1]>cnt:
                    dp[s-1]=cnt
                    new_q.append(s-1)
                    bt[s-1]=s
            if s<len(dp)-1:
                if dp[s+1]>cnt:
                    dp[s+1]=cnt
                    new_q.append(s+1)
                    bt[s+1]=s
            if s*2<len(dp):
                if dp[s*2]>cnt:
                    dp[s*2]=cnt
                    new_q.append(s*2)
                    bt[s*2]=s
        if end:
            break
        cnt+=1
        q=new_q
        new_q=[]
    ans=[]
    print(dp[m])
    while 1:
        ans.append(m)
        if m==n:
            break
        m=bt[m]
    ans.reverse()
print(*ans)
    

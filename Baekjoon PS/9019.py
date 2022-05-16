import sys
input=sys.stdin.readline
inf=100000
def d(n):
    return n*2%10000
def s(n):
    return n-1 if n!=0 else 9999
def l(n):
    tmp=n%1000
    tmp2=n//1000
    return tmp*10+tmp2
def r(n):
    tmp=n%10
    tmp2=n-tmp
    return tmp2//10 + tmp*1000
def dslr(n, m):
    dp=[inf for i in range(10000)]
    ans=[None for i in range(10000)]
    q=[n]
    ans[n]=''
    dp[n]=0
    q_new=[]
    cnt=1
    end=0
    while 1:
        while q:
            st=q.pop()
            if st==m:
                end=1
                break
            if dp[d(st)]>cnt:
                dp[d(st)]=cnt
                q_new.append(d(st))
                ans[d(st)]='D'
            if dp[s(st)]>cnt:
                dp[s(st)]=cnt
                q_new.append(s(st))
                ans[s(st)]='S'
            if dp[l(st)]>cnt:
                dp[l(st)]=cnt
                q_new.append(l(st))
                ans[l(st)]='L'
            if dp[r(st)]>cnt:
                dp[r(st)]=cnt
                q_new.append(r(st))
                ans[r(st)]='R'
        if end:
            break
        cnt+=1
        q=q_new
        q_new=[]
    move=''
    tmp=m
    while 1:
        move+=ans[tmp]
        if tmp==n:
            break
        elif ans[tmp]=='L':
            tmp=r(tmp)
        elif ans[tmp]=='R':
            tmp=l(tmp)
        elif ans[tmp]=='D':
            a=tmp//2
            b=(tmp+10000)//2
            if dp[tmp]-dp[a]==1:
                tmp=a
            else:
                tmp=b
        else:
            if tmp==9999:
                tmp=0
            else:
                tmp+=1

    print(*move[::-1], sep='')


t=int(input())
for i in range(t):
    n, m=map(int, input().split())
    dslr(n ,m)
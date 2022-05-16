import sys
input=sys.stdin.readline

n=int(input())
for i in range(n):
    a, b=map(int, input().split())
    if a%10==0:
        print(10)
    else:
        a=a%10
        ans=1
        for j in range(b):
            ans*=a
            ans=ans%10
        print(ans)
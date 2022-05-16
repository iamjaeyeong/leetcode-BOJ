import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
def func2(n, m):
    max_m=1
    while(1):
        if max_m**2>n:
            max_m-=1
            break
        max_m+=1
    if max_m>m:
        max_m=m
    cnt=0
    for k in range(1, max_m+1):
        if k**2>n:
            break
        if ((n-k**2)/k)+k > m:
            cnt+=(m-k)*2+1
        else:
            cnt+=((n-k**2)//k)*2+1
    return cnt

def func3(n, m):
    n-=1
    max_m=1
    while(1):
        if max_m**2>n:
            max_m-=1
            break
        max_m+=1
    if max_m>m:
        max_m=m
    cnt=0
    for k in range(1, max_m+1):
        if k**2>n:
            break
        if ((n-k**2)/k)+k > m:
            cnt+=(m-k)*2+1
        else:
            cnt+=((n-k**2)//k)*2+1
    return cnt

def func(start, end, m, k):
    if end==start:
        return start
    n=(start+end)//2
    below=func2(n, m)
    under=func3(n, m)
    if k<=under:
        return func(start, n-1, m ,k)
    elif under<k<=below:
        return n
    elif k>below:
        return func(n+1, end, m, k)
print(func(1, n**2, n, m))
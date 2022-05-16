import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**4)
def func(wire, k, start, end):
    if start==end:
        return start
    mid=(start+end)//2
    cnt=0
    for i in wire:
        cnt+=i//mid
    if cnt>=k:
        if end-mid==1:
            cnt=0
            for i in wire:
                cnt+=i//end
            if cnt>=k:
                return end
            else:
                return mid
        return func(wire, k, mid, end)
    else:
        return func(wire, k, start, mid-1)
n, k=map(int, input().split())
wire=[]
for i in range(n):
    wire.append(int(input()))
mx=max(wire)
print(func(wire, k, 1, mx))

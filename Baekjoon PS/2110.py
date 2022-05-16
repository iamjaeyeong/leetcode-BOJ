import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)
def mergesort(lst):
    if len(lst)<2:
        return lst
    else:
        mid=len(lst)//2
        left=mergesort(lst[:mid])
        right=mergesort(lst[mid:])
        return merge(left, right)

def merge(lst1, lst2):
    one_idx=0
    two_idx=0
    ret=[]
    while(1):
        if one_idx==len(lst1):
            ret+=lst2[two_idx:]
            return ret
        elif two_idx==len(lst2):
            ret+=lst1[one_idx:]
            return ret
        else:
            if lst1[one_idx]>lst2[two_idx]:
                ret.append(lst2[two_idx])
                two_idx+=1
            else:
                ret.append(lst1[one_idx])
                one_idx+=1


def check(houses, interval, tmp):
    cnt=1
    std=houses[0]
    for i in houses:
        if i-std>=interval:
            std=i
            cnt+=1
    if cnt>=tmp:
        return 1
    else:
        return 0

def func(houses,m, mn, mx):
    if mn==mx:
        return mn
    mid=(mx+mn)//2
    if check(houses, mid, m):
        if mid+1==mx:
            if check(houses, mx, m):
                return mx
            else:
                return mid
        return func(houses, m ,mid, mx)
    else:
        return func(houses, m, mn, mid-1)
    

n, m=map(int, input().split())
houses=[]
for i in range(n):
    houses.append(int(input()))
houses=mergesort(houses)
print(func(houses, m, 1, max(houses)-min(houses)))

import sys
input=sys.stdin.readline

def bisearch(lst, start, end, std):
    if end-start==0:
        return -1
    if end-start==1:
        if std>=lst[start]:
            return start
        else:
            return start-1
    else:
        mid=(start+end)//2
        if std>=lst[mid]:
            return bisearch(lst, mid, end, std)
        elif std<lst[mid]:
            return bisearch(lst, start, mid, std)


def merge(lst1, lst2, bag):
    ret=[]
    for i in lst1:
        for j in lst2:
            if i+j<=bag:
                ret.append(i+j)
    return ret


def recursion(weights, start, end, bag):
    # start=0, end=len(weights)
    if end-start>2:
        mid=(start+end)//2
        left=recursion(weights, start, mid, bag)
        right=recursion(weights, mid, end, bag)
        return merge(left, right, bag)
    else:
        if end-start==2:
            return [0, weights[start], weights[end-1], weights[start]+weights[end-1]]
        elif end-start==1:
            return [0, weights[start]]
        else:
            return []


n, bag=map(int, input().split())
weights=list(map(int, input().split()))
weights.sort()
left=recursion(weights, 0, len(weights)//2, bag)
right=recursion(weights, len(weights)//2, len(weights), bag)
left.sort()
right.sort()
ans=0
idx=len(right)-1
if left==[]:
    for i in right:
        if i<=bag:
            ans+=1
else:
    for i in left:
        idx=bisearch(right, 0, idx+1, bag-i)
        ans+=idx+1
print(ans)





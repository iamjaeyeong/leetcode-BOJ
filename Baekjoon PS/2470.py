import sys, math
input=sys.stdin.readline

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

n=int(input())
lst=list(map(int, input().split()))
lst=mergesort(lst)
p1=0
p2=n-1
ans=math.inf
ans_lst=[]
while(1):
    if p1>=p2:
        break
    tmp=lst[p1]+lst[p2]
    if ans>abs(tmp):
        ans=abs(tmp)
        ans_lst=[lst[p1], lst[p2]]
    if tmp>0:
        p2-=1
    else:
        p1+=1
print(*ans_lst)
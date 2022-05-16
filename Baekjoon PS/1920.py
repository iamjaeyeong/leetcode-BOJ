import sys
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

def find(lst, i, start, end , cnt):
    if end-start==1:
        if lst[start]!=i:
            pass
        else:
            cnt[0]+=1
    elif end==start:
        return
    else:
        if lst[start]==lst[end-1]==i:
            cnt[0]+=(end-start)
        else:
            mid=(end+start)//2
            if lst[mid]<i:
                find(lst, i, mid, end, cnt)
            elif lst[mid]>i:
                find(lst, i, start, mid, cnt)
            else:
                find(lst, i, mid, end,cnt)
                find(lst, i, start, mid, cnt)


n=input()
lst=list(map(int, input().split()))
m=input()
lst2=list(map(int, input().split()))
lst=mergesort(lst)
for i in lst2:
    cnt=[0]
    find(lst, i, 0, len(lst), cnt)
    print(cnt[0], end=' ')

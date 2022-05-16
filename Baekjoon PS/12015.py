import sys
input=sys.stdin.readline

n=input()
lst=list(map(int, input().split()))
def binary_search(lst, i, start, end):
    if start==end-1:
        if lst[start]<i:
            return start+1
        elif lst[start]==i:
            return -1
        else:
            return start
    mid=(start+end)//2
    if lst[mid]>i:
        return binary_search(lst, i, start=start, end=mid)
    elif lst[mid]==i:
        return -1
    else:
        return binary_search(lst, i, start=mid, end=end)
    
bs=[]
for i in lst:
    if bs==[]:
        bs.append(i)
    else:
        if bs[-1]<i:
            bs.append(i)
        else:
            idx=binary_search(bs, i, 0, len(bs))
            if idx==-1:
                continue
            else:
                bs[idx]=i
print(len(bs))
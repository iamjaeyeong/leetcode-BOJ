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

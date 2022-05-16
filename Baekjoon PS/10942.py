import sys
input=sys.stdin.readline

n=int(input())
lst=list(map(int, input().split()))

def palindrome(mid, lst):
    ret=0
    while(1):
        if mid-ret<0 or mid+ret>=len(lst):
            ret-=1
            break
        else:
            if lst[mid+ret]==lst[mid-ret]:
                ret+=1
            else:
                ret-=1
                break
    return ret

def palindrome2(start, end, lst):
    ret=0
    while(1):
        if start-ret<0 or end+ret>=len(lst):
            break
        else:
            if lst[start-ret]==lst[end+ret]:
                ret+=1
            else:
                break
    return ret

pal_odd=[]
for i in range(len(lst)):
    pal_odd.append(palindrome(i, lst))

pal_even=[]
for i in range(len(lst)-1):
    tmp=palindrome2(i, i+1, lst)
    if tmp==0:
        pal_even.append(-1)
    else:
        pal_even.append(tmp)

m=int(input())
for i in range(m):
    s, e=map(int, input().split())
    s-=1
    e-=1
    idx=s+e
    if idx%2:
        idx=idx//2
        if pal_even[idx]==-1:
            print(0)
        else:
            if e<=idx+pal_even[idx]:
                print(1)
            else:
                print(0)
    else:
        idx=idx//2
        if e<=pal_odd[idx]+idx:
            print(1)
        else:
            print(0)


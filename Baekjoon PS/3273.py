import sys
input=sys.stdin.readline
n=int(input())
lst=list(map(int, input().split()))

def sort(lst):
    tmp=[0 for i in range(1000001)]
    for i in lst:
        tmp[i]+=1
    ret=[]
    for i in range(1, len(tmp)):
        if tmp[i]==0:
            continue
        else:
            for j in range(tmp[i]):
                ret.append(i)
    return ret

lst=sort(lst)
target=int(input())
p1=0
p2=len(lst)-1
cnt=0
while(1):
    if p1>=p2:
        break
    if lst[p1]+lst[p2]>target:
        p2-=1
    elif lst[p1]+lst[p2]<target:
        p1+=1
    else:
        p1_tmp=1
        p2_tmp=1
        while(1):
            if p1+p1_tmp<p2 and lst[p1]==lst[p1+p1_tmp]:
                p1_tmp+=1
            else:
                break
        while(1):
            if p2-p2_tmp>p1 and lst[p2]==lst[p2-p2_tmp]:
                p2_tmp+=1
            else:
                break
        cnt+=(p1_tmp+p2_tmp-1)
        p1+=p1_tmp
        p2-=p2_tmp
print(cnt)


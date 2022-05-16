import sys
input=sys.stdin.readline

t=int(input())
n=input()
a=list(map(int, input().split()))
m=input()
b=list(map(int, input().split()))


a_sum=[]
for i in range(1, len(a)+1):
    for j in range(len(a)-i+1):
        a_sum.append(t-sum(a[j:j+i]))


b_sum=[]
b_sum_cnt={}
for i in range(1, len(b)+1):
    for j in range(len(b)-i+1):
        b_sum.append(sum(b[j:j+i]))


b_sum.sort()
for i in range(len(b_sum)):
    if i!=0 and b_sum[i-1]==b_sum[i]:
        b_sum_cnt[b_sum[i]]+=1
    else:
        b_sum_cnt[b_sum[i]]=1

def binary_search(lst, s, e, target):
    if e-s==1:
        if lst[s]!=target:
            return -1
        else:
            return 1
    if e-s==0:
        return -1
    mid=(s+e)//2
    if lst[mid]>target:
        return binary_search(lst, s, mid, target)
    elif lst[mid]==target:
        return mid
    else:
        return binary_search(lst, mid+1, e, target)

ans=0
for i in a_sum:
    if binary_search(b_sum, 0, len(b_sum), i)==-1:
        continue
    else:
        ans+=b_sum_cnt[i]

print(ans)
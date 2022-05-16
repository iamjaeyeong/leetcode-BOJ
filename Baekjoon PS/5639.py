import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def bs(s, e, std):
    if s==e:
        return s
    elif e-s==1:
        if pre[s]>std:
            return s
        else:
            return e
    else:
        mid=(s+e)//2
        if pre[mid]>std:
            return bs(s, mid, std)
        else:
            return bs(mid, e, std)


def func(s, e, ans):
    ans.append(pre[s])
    idx=bs(s+1, e+1, pre[s])
    if e>=idx:
        func(idx, e, ans)
    if idx-1>=s+1:
        func(s+1, idx-1, ans)
pre=[]
while 1:
    try:
        pre.append(int(input()))
    except:
        break
ans=[]
func(0, len(pre)-1, ans)
for i in range(len(ans)-1, -1 ,-1):
    print(ans[i])




# root left right
# left right root
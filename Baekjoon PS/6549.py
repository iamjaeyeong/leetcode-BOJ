import sys, math
input=sys.stdin.readline
inf=math.inf
sys.setrecursionlimit(10**6)
def seg(lst):
    depth=0
    while(1):
        if pow(2, depth)>=len(lst):
            depth+=1
            break
        depth+=1
    tree=[inf for i in range(pow(2, depth))]
    depth-=1
    s=pow(2, depth)
    for i in range(0, len(lst)):
        if i==len(lst):
            break
        tree[s+i]=(lst[i], i)
    for _ in range(depth):
        s=s//2
        for i in range(0, s):
            idx=s+i
            if tree[idx*2]==inf:
                break
            elif tree[idx*2+1]==inf:
                tree[idx]=tree[idx*2]
                break
            else:
                if tree[idx*2][0]>tree[idx*2+1][0]:
                    tree[idx]=tree[idx*2+1]
                else:
                    tree[idx]=tree[idx*2]
    tree[0]=None
    return tree, depth

def find(tree, start, end, s, e, idx): #tree, 찾는 범위 시작점, 끝점, s=0, e=pow(2,depth), idx=
    if s>e:
        return inf
    elif start<=s and e<=end:
        return tree[idx]
    elif start>e or s>end:
        return inf
    else:
        mid=(s+e)//2
        if end<=mid:
            return find(tree, start, end, s, mid, idx*2)
        elif start>mid:
            return find(tree, start, end, mid+1, e, idx*2+1)
        else:
            a=find(tree, start, end, s, mid, idx*2)
            b=find(tree, start, end, mid+1, e, idx*2+1)
            if a==inf:
                return b
            elif b==inf:
                return a
            elif a[0]>b[0]:
                return b
            else:
                return a


def histogram(tree, start, end, area, depth):
    if start>end:
        pass
    elif end-start==1:
        area[0]=max(area[0], min(lst[start], lst[start+1])*2, max(lst[start], lst[start+1]))
    elif end==start:
        area[0]=max(area[0], lst[start])
    else:
        tmp=find(tree, start, end, 0, pow(2,depth)-1, 1)
        area[0]=max(area[0], (end-start+1)*tmp[0])
        histogram(tree, start, tmp[1]-1, area, depth)
        histogram(tree, tmp[1]+1, end, area, depth)


while(1):
    lst=list(map(int, input().split()))
    if lst[0]==0:
        break
    elif lst[0]==1:
        print(lst[1])
        continue
    else:
        lst=lst[1:]
        tree, depth= seg(lst)
        area=[0]
        histogram(tree, 0, len(lst)-1, area, depth)
        print(area[0])
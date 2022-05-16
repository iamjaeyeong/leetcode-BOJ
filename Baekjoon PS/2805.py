import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

def func(trees, m , start ,end):
    if start==end:
        return start
    else:
        mid=(start+end)//2
        cnt=0
        for tree in trees:
            if tree-mid>=0:
                cnt+=tree-mid
        if cnt>=m:
            if end-mid==1:
                cnt=0
                for tree in trees:
                    if tree-mid>=0:
                        cnt+=tree-end
                if cnt>=m:
                    return end
                else:
                    return mid
            else:
                return func(trees, m, mid, end)
        else:
            return func(trees, m, start ,mid-1)

n, m=map(int, input().split())
trees=list(map(int, input().split()))
print(func(trees, m, 1, max(trees)))
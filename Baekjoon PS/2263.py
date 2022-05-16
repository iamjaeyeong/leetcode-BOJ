import sys
input=sys.stdin.readline
sys.setrecursionlimit(500000)

def func(s1, e1, s2, e2):
    if s1==e1:
        print(lst1[s1], end=' ')
    elif e1>s1:
        root=lst2[e2]
        tmp=idx[root]
        print(root, end=' ')
        func(s1, tmp-1, s2, s2+(tmp-1-s1))
        func(tmp+1, e1, s2+(tmp-s1), e2-1)


n=int(input())
lst1=list(map(int, input().split()))
lst2=list(map(int, input().split()))
idx=[-1 for i in range(n+1)]
for i in range(n):
    idx[lst1[i]]=i
func(0, n-1, 0, n-1)
# 2263 <트리의 순회>


import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline()

n=int(input())
inorder=list(map(int, input().split()))
postorder=list(map(int, input().split()))
root=postorder[-1]
# inorder 원소들 어딨는지 알기 쉽게 하기 위해 따로 저장
pos=[0]*(n+1)

for i in range(n):
    pos[inorder[i]]=i

def divide(s, e, s2, e2):
    if e-s==1 or e2-s2==1:
        print(postorder[s], end=' ')
    elif e-s>1 or e2-s2>1:
        root=postorder[e2-1]
        print(root, end=' ')
        tmp=pos[root]

        divide(s, tmp, s2, s2+tmp-s)
        divide(tmp+1, e, s2+tmp-s+1, e2-1)
        return

divide(0,n,0,n)
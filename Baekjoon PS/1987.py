import sys

from matplotlib.style import available
input=sys.stdin.readline

r, c=map(int, input().split())
board=[]
for i in range(r):
    board.append(input().rstrip()[:20])
ans=[0]

def dfs(pos, available, cnt):
    x=pos[0]
    y=pos[1]
    end=1
    if x>0 and available[ord(board[x-1][y])-65]==0:
        available[ord(board[x-1][y])-65]=1
        dfs([x-1, y], available, cnt+1)
        available[ord(board[x-1][y])-65]=0
        end=0
    if y>0 and available[ord(board[x][y-1])-65]==0:
        available[ord(board[x][y-1])-65]=1
        dfs([x, y-1], available, cnt+1)
        available[ord(board[x][y-1])-65]=0
        end=0
    if x<len(board)-1 and available[ord(board[x+1][y])-65]==0:
        available[ord(board[x+1][y])-65]=1
        dfs([x+1, y], available, cnt+1)
        available[ord(board[x+1][y])-65]=0
        end=0
    if y<len(board[0])-1 and available[ord(board[x][y+1])-65]==0:
        available[ord(board[x][y+1])-65]=1
        dfs([x, y+1], available, cnt+1)
        available[ord(board[x][y+1])-65]=0
        end=0
    if end:
        if ans[0]<cnt:
            ans[0]=cnt
available=[0 for i in range(26)]
available[ord(board[0][0])-65]=1
dfs([0, 0], available, 1)
print(ans[0])

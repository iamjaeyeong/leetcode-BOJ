from collections import deque
import sys
input=sys.stdin.readline

n, m= map(int, input().split())
board=[]
for i in range(n):
    board.append(list(map(int, input().rstrip())))
board[0][0]=-1
deq=deque()
deq.append(deque())
deq.append(deque())
deq[0].append([0,0,1, -1])
cnt=1
while(1):
    if len(deq[0])==0:
        if len(deq[1])==0:
            cnt=-1
            break
        deq.popleft()
        deq.append(deque())
        cnt+=1
    pos=deq[0].popleft()
    if pos[0]==n-1 and pos[1]==m-1:
        break
    else:
        if pos[0]>0:
            if board[pos[0]-1][pos[1]]==0 or (pos[2]==1 and board[pos[0]-1][pos[1]]==-2):
                deq[1].append([pos[0]-1, pos[1], pos[2], pos[3]])
                board[pos[0]-1][pos[1]]=pos[3]
            if board[pos[0]-1][pos[1]]==1 and pos[2]==1:
                deq[1].append([pos[0]-1, pos[1], 0, -2])
                board[pos[0]-1][pos[1]]=pos[3]
        if pos[1]>0:
            if board[pos[0]][pos[1]-1]==0 or (pos[2]==1 and board[pos[0]][pos[1]-1]==-2):
                deq[1].append([pos[0], pos[1]-1, pos[2], pos[3]])
                board[pos[0]][pos[1]-1]=pos[3]
            if board[pos[0]][pos[1]-1]==1 and pos[2]==1:
                deq[1].append([pos[0], pos[1]-1, 0, -2])
                board[pos[0]][pos[1]-1]=pos[3]
        if pos[0]<n-1:
            if board[pos[0]+1][pos[1]]==0 or (pos[2]==1 and board[pos[0]+1][pos[1]]==-2):
                deq[1].append([pos[0]+1, pos[1], pos[2], pos[3]])
                board[pos[0]+1][pos[1]]=pos[3]
            if board[pos[0]+1][pos[1]]==1 and pos[2]==1:
                deq[1].append([pos[0]+1, pos[1], 0, -2])
                board[pos[0]+1][pos[1]]=pos[3]
        if pos[1]<m-1:
            if board[pos[0]][pos[1]+1]==0 or (pos[2]==1 and board[pos[0]][pos[1]+1]==-2):
                deq[1].append([pos[0], pos[1]+1, pos[2], pos[3]])
                board[pos[0]][pos[1]+1]=pos[3]
            if board[pos[0]][pos[1]+1]==1 and pos[2]==1:
                deq[1].append([pos[0], pos[1]+1, 0, -2])
                board[pos[0]][pos[1]+1]=pos[3]
print(cnt)


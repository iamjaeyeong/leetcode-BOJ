import sys
input=sys.stdin.readline

board=[[0 for j in range(9)] for i in range(9)]
for i in range(9):
    tmp=input().rstrip()
    for j in range(9):
        board[i][j]=int(tmp[j])
square=[[i for i in range(9)] for j in range(9)]
col=[[i for i in range(9)] for j in range(9)]
row=[[i for i in range(9)] for j in range(9)]

for r in range(9):
    for c in range(9):
        if board[r][c]!=0:
            row[r][board[r][c]-1]=100
            col[c][board[r][c]-1]=100

for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                if board[i*3+k][j*3+l]!=0:
                    square[i*3+j][board[i*3+k][j*3+l]-1]=100

def dfs(r, c, stop):
    if r==9:
        stop[0]=1
        return
    square_num=(r//3)*3+(c//3)
    new_r, new_c=r+(c+1)//9, (c+1)%9
    if board[r][c]==0:
        filler=[]
        for i in range(9):
            if square[square_num][i]!=100 and row[r][i]!= 100 and col[c][i]!=100:
                filler.append(i)
        for i in filler:
            board[r][c]=i+1
            square[square_num][i]=100
            row[r][i]=100
            col[c][i]=100
            dfs(new_r, new_c,stop)
            if stop[0]:
                return
            board[r][c]=0
            square[square_num][i]=i
            row[r][i]=i
            col[c][i]=i
    else:
        dfs(new_r, new_c, stop)
dfs(0, 0, [0])
for i in board:
    print(*i, sep='')

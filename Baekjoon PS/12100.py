import sys
input=sys.stdin.readline

n_rows=int(input())
board=[]

for i in range(n_rows):
    board.append(list(map(int, input().split())))

def merge_left(board, r):
    prev = board[r][0]
    prev_idx = 0
    c = 1
    while c<len(board):
        if board[r][c]==0:
            c += 1
            continue
        if board[r][c]==prev:
            board[r][prev_idx] = prev*2
            board[r][c] = 0
            prev = None
        else:
            prev = board[r][c]
            prev_idx = c
        c += 1

def merge_right(board, r):
    prev = board[r][len(board)-1]
    prev_idx = len(board)-1
    c = len(board)-2
    while c>=0:
        if board[r][c]==0:
            
            c -= 1
            continue
        if board[r][c]==prev:
            board[r][prev_idx] = prev*2
            board[r][c] = 0
            prev = None
        else:
            prev = board[r][c]
            prev_idx = c
        c -= 1
        
def merge_up(board, c):
    prev = board[0][c]
    prev_idx = 0
    r = 1
    while r<len(board):
        if board[r][c]==0:
            r += 1
            continue
        if board[r][c]==prev:
            board[prev_idx][c] = prev*2
            board[r][c] = 0
            prev = None
        else:
            prev = board[r][c]
            prev_idx = r
        r += 1
        
def merge_down(board, c):
    prev = board[len(board)-1][c]
    prev_idx = len(board)-1
    r = len(board)-2
    while r>=0:
        if board[r][c]==0:
            r -= 1
            continue
        if board[r][c]==prev:
            board[prev_idx][c] = prev*2
            board[r][c] = 0
            prev = None
        else:
            prev = board[r][c]
            prev_idx = r
        r -= 1
            
def move_left(board, r):
    idx = 0
    for c in range(len(board)):
        if board[r][idx]:
            idx += 1
            continue
        else:
            if board[r][c]:
                board[r][idx] = board[r][c]
                board[r][c] = 0
                idx += 1  
                
def move_right(board, r):
    idx = len(board)-1
    for c in range(len(board)-1, -1, -1):
        if board[r][idx]:
            idx -= 1
            continue
        else:
            if board[r][c]:
                board[r][idx] = board[r][c]
                board[r][c] = 0
                idx -= 1 
                
def move_up(board, c):
    idx = 0
    for r in range(len(board)):
        if board[idx][c]:
            idx += 1
            continue
        else:
            if board[r][c]:
                board[idx][c] = board[r][c]
                board[r][c] = 0
                idx += 1  
                
def move_down(board, c):
    idx = len(board)-1
    for r in range(len(board)-1, -1, -1):
        if board[idx][c]:
            idx -= 1
            continue
        else:
            if board[r][c]:
                board[idx][c] = board[r][c]
                board[r][c] = 0
                idx -= 1 
                
cases = [board]
for i in range(5):
    new_cases = []
    for case in cases:
        new_case = [[i for i in j] for j in case]
        for i in range(len(board)):
            merge_up(new_case, i)
            move_up(new_case, i)
        new_cases.append(new_case)
        
        new_case = [[i for i in j] for j in case]
        for i in range(len(board)):
            merge_down(new_case, i)
            move_down(new_case, i)
        new_cases.append(new_case)
        
        new_case = [[i for i in j] for j in case]
        for i in range(len(board)):
            merge_right(new_case, i)
            move_right(new_case, i)
        new_cases.append(new_case)
        
        new_case = [[i for i in j] for j in case]
        for i in range(len(board)):
            merge_left(new_case, i)
            move_left(new_case, i)
        new_cases.append(new_case)
    cases = new_cases

def return_max(board):
    return max([max(i) for i in board])

answer = 0
maximums = [return_max(case) for case in cases]
answer = max(maximums)
print(answer)

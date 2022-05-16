import sys
input=sys.stdin.readline


n_rows=int(input())
board=[]

for i in range(n_rows):
    board.append(list(map(int, input().split())))


def move(board_, direction, moves):
    for i in board_:
        print(i)
    a, b, c, d=0, 0, 0, 0
    if direction=='up':
        cop=[]
        for i in board_:
            cop.append(i[:])
        a=up(cop, moves-1)
    elif direction=='left':
        cop=[]
        for i in board_:
            cop.append(i[:])
        b=left(cop, moves-1)
    elif direction=='right':
        cop=[]
        for i in board_:
            cop.append(i[:])
        c=right(cop, moves-1)
    else:
        cop=[]
        for i in board_:
            cop.append(i[:])
        d=down(cop, moves-1)
    return max(a, b, c, d)

def merge_row(row):
    return

def merge_col(col, c):
    return

# move 0일 때 빼는걸 move 함수에서 처리하자.

def up(board_, moves):
    print('up')
    for c in range(n_rows):
        merge_col(board_, c)
    for i in ['up', 'left', 'right', 'down']:
        return move(board_, i, moves)

def down(board_, moves):
    print('down')
    for c in range(n_rows):
        merge_col(board_,c)
    for i in ['up', 'left', 'right', 'down']:
        return move(board_, i, moves)

def right(board_, moves):
    print('right')
    for r in range(n_rows):
        board_[r]=merge_row(board_[r])
    for i in ['up', 'left', 'right', 'down']:
        return move(board_, i, moves)

def left(board_, moves):
    print('left')
    for r in range(n_rows):
        board_[r]=merge_row(board_[r])
    for i in ['up', 'left', 'right', 'down']:
        return move(board_, i, moves)

 
for i in ['up', 'left', 'right', 'down']:
    print(move(board, i, 5))


print(move(board, 'left', 1))


import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(input())
    
blue_pos = [0, 0]
red_pos = [0, 0]
for i in range(n):
    for j in range(m):
        if board[i][j]=='R':
            red_pos = [i, j]
        if board[i][j]=='B':
            blue_pos = [i, j]

def right(board, pos):
    for i in range(pos[1], len(board[0])):
        if board[pos[0]][i]=='#':
            return [pos[0], i-1]
        elif board[pos[0]][i]=='O':
            return [-1, -1]
    return [pos[0], len(board[0]-1)]

def left(board, pos):
    for i in range(pos[1], -1, -1):
        if board[pos[0]][i]=='#':
            return [pos[0], i+1]
        elif board[pos[0]][i]=='O':
            return [-1, -1]
    return [pos[0], 0]

def up(board, pos):
    for i in range(pos[0], -1, -1):
        if board[i][pos[1]]=='#':
            return [i+1, pos[1]]
        elif board[i][pos[1]]=='O':
            return [-1, -1]
    return [0, pos[1]]

def down(board, pos):
    for i in range(pos[0], len(board)):
        if board[i][pos[1]]=='#':
            return [i-1, pos[1]]
        elif board[i][pos[1]]=='O':
            return [-1, -1]
    return [len(board), pos[1]]

stack = [[blue_pos, red_pos]]
# before_move = [0, 0, 0, 0]
# direction_dict = {0:1, 1:0, 2:3, 3:2}
answer = -1
for i in range(10):
    next_stack = []
    for blue, red in stack:
        b_moves = [left(board, blue), right(board, blue), up(board, blue), down(board, blue)]
        r_moves = [left(board, red), right(board, red), up(board, red), down(board, red)]
        if blue[1]==red[1] and b_moves[2]==r_moves[2]:
            if blue[0]>red[0]:
                b_moves[2][0] += 1
                r_moves[3][0] -= 1
            else:
                r_moves[2][0] += 1
                b_moves[3][0] -= 1
        if blue[0]==red[0] and b_moves[0]==r_moves[0]:
            if blue[1]>red[1]:
                b_moves[0][1] += 1
                r_moves[1][1] -= 1
            else:
                r_moves[0][1] += 1
                b_moves[1][1] -= 1
        # print(blue, b_moves)
        # print(red, r_moves)
        # print()
        # move_history = [0, 0, 0, 0]
        for direction, (b_move, r_move) in enumerate(zip(b_moves, r_moves)):
            # if before_move[direction_dict[direction]]:
            #     continue
            if blue==b_move and red==r_move:
                continue
            elif b_move[0]==-1 or b_move[1]==-1:
                continue
            elif r_move[0]==-1 or r_move[1]==-1:
                answer = i + 1
                break
            else:
                next_stack.append([b_move, r_move])
                # move_history[direction] = 1
    if answer!=-1:
        break
    stack = next_stack
    # before_move = move_history
    # print(i+1, stack)
    # print(before_move)
    # print()
print(answer)


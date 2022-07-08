class Solution:
    def solveSudoku(self, board) -> None:
        zero_pos = []
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    board[i][j] = 0
                else:
                    board[i][j] = int(board[i][j])
        
        def find_candidates(board, col, row):
            ret = [1 for i in range(10)]
            for i in board[row]:
                ret[i-1] = 0
            for i in range(9):
                ret[board[i][col]-1] = 0
            col = col//3*3
            row = row//3*3
            for i in range(3):
                for j in range(3):
                    ret[board[row+i][col+j]-1] = 0
                
            ret.pop()
            ret = [i+1 for i in range(9) if ret[i]]
            return ret
        
        def check(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j]==0:
                        return False
            return True
        
        
        def dfs(board, cnt, zero_pos):
            if cnt==len(zero_pos):
                return 1
            col = zero_pos[cnt][0]
            row = zero_pos[cnt][1]

            candidates = find_candidates(board, col, row)
            for candidate in candidates:
                board[row][col] = candidate
                if dfs(board, cnt+1, zero_pos):
                    return 1
            board[row][col] = 0
        
        while 1:
            stop = 1
            for i in range(9):
                for j in range(9):
                    if board[i][j]==0:
                        candidates = find_candidates(board, j, i)
                        if len(candidates)==1:
                            board[i][j] = candidates[0]
                            stop = 0
            if stop:
                break
        
        for i in range(9):
            for j in range(9):
                if board[i][j]==0:
                    zero_pos.append([j, i])
                    
        dfs(board, 0, zero_pos)
        
        for i in range(9):
            for j in range(9):
                board[i][j] = str(board[i][j])
        
                    
        
class Solution:
    def totalNQueens(self, n: int):
        solution = [0]
        board = [[0 for i in range(n)] for j in range(n)]
        def dfs(board, queen, solution=solution):
            if len(queen)==len(board):
                solution[0] += 1
            else:
                row = len(queen)
                for i in range(len(board)):
                    if board[row][i]:
                        continue
                    else:
                        stack = []
                        cnt = 1
                        while 1:
                            if row+cnt>=len(board):
                                break
                            if board[row+cnt][i]==0:
                                stack.append([row+cnt, i])
                                board[row+cnt][i] = 1
                            cnt += 1
                        cnt = 1
                        while 1:
                            if i+cnt>=len(board) or row+cnt>=len(board):
                                break
                            if board[row+cnt][i+cnt]==0:
                                stack.append([row+cnt, i+cnt])
                                board[row+cnt][i+cnt] = 1
                            cnt += 1
                        cnt = 1
                        while 1:
                            if row+cnt>=len(board) or i-cnt<0:
                                break
                            if board[row+cnt][i-cnt]==0:
                                stack.append([row+cnt, i-cnt])
                                board[row+cnt][i-cnt] = 1
                            cnt += 1
                        dfs(board, queen+[i], solution=solution)
                        for pos in stack:
                            board[pos[0]][pos[1]] = 0
        dfs(board, [], solution=solution)
                
        return solution[0]
                        
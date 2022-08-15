class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def bfs(board, visit):
            if visit==[]:
                return
            elif visit[0][0]==len(board)-1 and visit[0][1]==len(board[0])-1:
                if len(board)==1 and len(board[0])==1:
                    board[-1][-1] = board[-1][-2] + board[-2][-1]
                elif len(board)==1:
                    board[-1][-1] = board[-1][-2]
                elif len(board[0])==1:
                    board[-1][-1] = board[-2][-1]
                else:
                    board[-1][-1] = board[-2][-1] + board[-1][-2]
                return
            else:
                next_visit = set()
                for v in visit:
                    if v[0]==0:
                        print(v)
                        board[v[0]][v[1]] = board[v[0]][v[1]-1]
                    elif v[1]==0:
                        board[v[0]][v[1]] = board[v[0]-1][v[1]]
                    else:
                        board[v[0]][v[1]] = board[v[0]][v[1]-1] + board[v[0]-1][v[1]]

                    if v[0]==len(board)-1:
                        next_visit.add((v[0], v[1]+1))
                    elif v[1]==len(board[0])-1:
                        next_visit.add((v[0]+1, v[1]))
                    else:
                        next_visit.add((v[0], v[1]+1))
                        next_visit.add((v[0]+1, v[1]))
                bfs(board, list(next_visit))
                
        board = [[0 for i in range(n)] for j in range(m)]
        visit = []
        board[0][0] = 1
        if m>1:
            visit.append((1, 0))
        if n>1:
            visit.append((0, 1))
        bfs(board, visit)
        return board[-1][-1]
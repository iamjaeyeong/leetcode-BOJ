class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        visits = []
        board = [[0 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
        if obstacleGrid[0][0]!=1:
            board[0][0] = 1
            if len(obstacleGrid)>1:
                visits.append((1, 0))
            if len(obstacleGrid[0])>1:
                visits.append((0, 1))
        
        while 1:
            if len(visits)==0 or visits[0]==(len(obstacleGrid)-1, len(obstacleGrid[0])-1):
                break
            next_visits = set()
            for visit in visits:
                if obstacleGrid[visit[0]][visit[1]]:
                    continue
                if visit[0]==0:
                    board[visit[0]][visit[1]] += board[visit[0]][visit[1]-1]
                elif visit[1]==0:
                    board[visit[0]][visit[1]] += board[visit[0]-1][visit[1]]
                else:
                    board[visit[0]][visit[1]] += (board[visit[0]-1][visit[1]]+board[visit[0]][visit[1]-1])
                if visit[0]>=len(obstacleGrid)-1:
                    next_visits.add((visit[0], visit[1]+1))
                elif visit[1]>=len(obstacleGrid[0])-1:
                    next_visits.add((visit[0]+1, visit[1]))
                else:
                    next_visits.add((visit[0], visit[1]+1))
                    next_visits.add((visit[0]+1, visit[1]))
            visits = list(next_visits)
        

        if len(obstacleGrid)>1:
            board[-1][-1] += board[-2][-1]
        if len(obstacleGrid[0])>1:
            board[-1][-1] += board[-1][-2]

        if obstacleGrid[-1][-1]:
            board[-1][-1] = 0
        return board[-1][-1]
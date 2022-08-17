class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        visits = [(0, 0)]
        m = len(grid)
        n = len(grid[0])
        while 1:
            if visits[0]==(m-1, n-1):
                break
            next_visits = set()
            for visit in visits:
                if visit[0]+1 < m:
                    next_visits.add((visit[0]+1, visit[1]))
                if visit[1]+1 < n:
                    next_visits.add((visit[0], visit[1]+1))
                if visit[0]>0 and visit[1]>0:
                    grid[visit[0]][visit[1]] += min(grid[visit[0]-1][visit[1]], grid[visit[0]][visit[1]-1])
                elif visit[0]>0:
                    grid[visit[0]][visit[1]] += grid[visit[0]-1][visit[1]]
                elif visit[1]>0:
                    grid[visit[0]][visit[1]] += grid[visit[0]][visit[1]-1]
            visits = list(next_visits)
        answer = grid[-1][-1]
        if m>1 and n>1:
            answer += min(grid[-2][-1], grid[-1][-2])
        elif n>1:
            answer += grid[-1][-2]
        elif m>1:
            answer += grid[-2][-1]

        return answer
        
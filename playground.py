from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0: return 0
        
        m, n = len(grid), len(grid[0])
        answer = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    currentArea = self.BFS(grid, i, j)
                    answer = max(answer, currentArea)
        
        return answer
    
    def BFS(self, grid, x, y):
        q = deque([])
        q.append((x,y))

        dx = [1,0,0, -1]
        dy = [0, 1, -1, 0]
        area = 1
        grid[x][y] = 0
        while q:
            q.popleft()
            for k in range(4):
                X = x+dx[k]
                Y = y + dy[k]
                if X >= 0 and X < len(grid) and Y >= 0 and Y < len(grid[0]) and grid[X][Y] == 1:
                    q.append((X, Y))
                    area += 1
                    grid[X][Y] = 0

        return area
                


        
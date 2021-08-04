"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""

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
            i, j = q.popleft()
            for k in range(4):
                X = i+dx[k]
                Y = j + dy[k]
                if X >= 0 and X < len(grid) and Y >= 0 and Y < len(grid[0]) and grid[X][Y] == 1:
                    q.append((X, Y))
                    area += 1
                    grid[X][Y] = 0

        return area

test = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
result = test.maxAreaOfIsland(grid)
print(result)
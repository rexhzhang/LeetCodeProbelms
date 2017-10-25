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
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        maxArea = 0
        row,column = len(grid), len(grid[0])
        for y in range(row):
            for x in range(column):
                if grid[y][x] == 1:
                    currentArea = self.BFS(grid, y, x, row, column)
                    maxArea = max(currentArea, maxArea)

        return maxArea

    def BFS(self, grid, y, x, row, column):
        queue = deque([(y,x)])
        grid[y][x] = 0
        area = 1
        while queue:
            current = queue.popleft()
            currentY = current[0]
            currentX = current[1]
            dX = [1, 0, 0, -1]
            dY = [0, 1, -1, 0]
            for i in range(4):
                X = currentX + dX[i]
                Y = currentY + dY[i]
                if Y >= 0 and X >= 0 and Y < row and X < column and grid[Y][X] == 1:
                    area += 1
                    queue.append((Y,X))
                    grid[Y][X] = 0

        return area

test = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
result = test.maxAreaOfIsland(grid)
print(result)
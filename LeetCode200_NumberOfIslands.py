"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water
and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are
all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None or len(grid) == 0 or len(grid[0]) ==0:
            return 0

        row, column = len(grid), len(grid[0])
        count = 0
        for y in range(row):
            for x in range(column):
                if grid[y][x] == "1":
                    self.BFS(grid, y, x, row, column)
                    count += 1

        return count

    def BFS(self,grid, yy, xx, row, column):
        q = [[yy,xx]]
        while q:
            y, x = q.pop(0)
            dX = [0,0,1,-1]
            dY = [1,-1,0,0]
            for i in range(4):
                X = x + dX[i]
                Y = y + dY[i]

                if self.insideGrid(Y, X, row, column) and grid[Y][X] == "1":
                    q.append([Y,X])
                    grid[Y][X] = "0"

    def insideGrid(self, y, x, row, column):
        return y>=0 and x>=0 and y < row and x < column


test = Solution()
testcase = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
result = test.numIslands(testcase)
print(result)
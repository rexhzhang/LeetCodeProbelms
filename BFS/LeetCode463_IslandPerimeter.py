"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
"""
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None:
            return -1
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        row, column = len(grid), len(grid[0])

        def findNeighbors(grid, x, y, row, column):
            dX = [1,-1, 0, 0]
            dY = [0, 0, 1, -1]
            counter = 0
            for i in range(4):
                X = x + dX[i]
                Y = y + dY[i]
                if insideGrid(X, Y, row, column) and grid[Y][X] == 1:
                    counter += 1
            return counter

        def insideGrid(x, y, row, column):
            return x>= 0 and y>= 0 and x < column and y < row

        ans = 0
        for y in range(row):
            for x in range(column):
                if grid[y][x] == 1:
                    neighborsCount = findNeighbors(grid, x, y, row, column)
                    ans += (4 - neighborsCount)

        return ans



test = Solution()
grid = [[0,1,0,0], [1,1,1,0],  [0,1,0,0],  [1,1,0,0]]
result = test.islandPerimeter(grid)
print (result)




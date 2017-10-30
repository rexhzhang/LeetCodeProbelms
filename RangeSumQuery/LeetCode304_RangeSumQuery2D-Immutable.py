"""Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (
row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2,
col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""

"""The idea is simple, just precompute sums for all matrices with (0, 0) as top left corner and (i, j) as bottom 
right corner. There are O(n^2) of these matrices, so we store them in a 2D table. In order to make code simpler, 
I add an extra column and row, filled with 0 """

class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if matrix is None or not matrix:
            return
        row = len(matrix)
        column = len(matrix[0])
        if row == 0 or column == 0: return

        self.dp = [[0 for i in range(column + 1)] for j in range(row + 1)]
        for i in range(1, row+1):
            for j in range(1, column+1):
                self.dp[i][j] = matrix[i-1][j-1] + self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1]


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        row1, row2, col1, col2 = row1+1, row2+1, col1+1, col2+1
        return self.dp[row2][col2] - self.dp[row1-1][col2] - self.dp[row2][col1-1] + self.dp[row1-1][col1-1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
obj = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])

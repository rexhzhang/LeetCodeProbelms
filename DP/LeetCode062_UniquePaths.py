"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for x in range(n):
            matrix[0][x] = 1

        for y in range(m):
            matrix[y][0] = 1

        for y in range(1, m):
            for x in range(1, n):
                matrix[y][x] = matrix[y - 1][x] + matrix[y][x - 1]

        return matrix[m - 1][n - 1]
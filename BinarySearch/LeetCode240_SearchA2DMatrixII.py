"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""
"""
从右上角到左下角遍历，时间复杂度O(m+n)，空间复杂度O(1)
遍历每行，在每行中用binary search，时间复杂度O(mlogn)
在2的基础上，先对比行数和列数，然后遍历比较小的维度，二分搜索比较大的维度，时间复杂度 min ( O(mlogn), O(nlogm))
对比遍历和二分法，在行数列数接近的时候选用1， 在 m >> n 或者 n >> m的时候选择3
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 从右上角到左下角遍历，时间复杂度O(m+n)，空间复杂度O(1)
        if not matrix: return False
        if not matrix[0]: return False
        m, n = len(matrix), len(matrix[0])
        
        row, col = 0, n-1
        while row < m and col >= 0:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                return True
        
        return False
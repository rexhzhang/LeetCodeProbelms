"""
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Have you met this question in a real interview? Yes
Example
Consider the following matrix:

[
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
Given target = 3, return true.

Challenge
O(log(n) + log(m)) time
"""
class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0 or target is None: return False

        start = 0; end = len(matrix)*len(matrix[0]) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            x, y = mid % len(matrix[0]), mid / len(matrix[0])

            if matrix[y][x] == target:
                return True
            elif matrix[y][x] > target:
                end = mid
            else:
                start = mid
        x1,y1 = start % len(matrix[0]), start / len(matrix[0])
        x2, y2 = end % len(matrix[0]), end / len(matrix[0])
        if matrix[y1][x1] == target:
            return True
        elif matrix[y2][x2] == target:
            return True
        else:
            return False
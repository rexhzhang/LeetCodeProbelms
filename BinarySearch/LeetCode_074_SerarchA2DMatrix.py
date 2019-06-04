"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
            
        start, end = 0, len(matrix) * len(matrix[0]) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            x,y = mid//len(matrix[0]) ,mid%len(matrix[0])

            if matrix[x][y]==target:
                return True
            
            elif matrix[x][y] < target:
                start = mid
            
            else:
                end = mid
    
        if matrix[start//len(matrix[0])][start%len(matrix[0])] == target:
            return True
        
        elif matrix[end//len(matrix[0])][end%len(matrix[0])] == target:
            return True

        else:
            return False
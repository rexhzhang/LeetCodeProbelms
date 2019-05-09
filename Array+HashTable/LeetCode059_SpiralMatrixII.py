"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        
        answer = [[None for _ in range(n)] for _ in range(n)]
        
        start_row, end_row, start_column, end_column = 0, n-1, 0, n-1
        
        x = 1
        direction = 0
        while start_row <= end_row and start_column <= end_column:
            
            if direction  == 0:
                for i in range(start_column, end_column+1):
                    answer[start_row][i] = x
                    x += 1
                start_row += 1
            
            elif direction == 1:
                for i in range(start_row, end_row + 1):
                    answer[i][end_column] = x
                    x += 1
                end_column -= 1
            
            elif direction == 2:
                for i in range(end_column, start_column-1, -1):
                    answer[end_row][i] = x
                    x += 1
                end_row -= 1
            
            elif direction == 3:
                for i in range(end_row, start_row -1, -1):
                    answer[i][start_column] = x
                    x += 1
                start_column += 1
            
            direction = (direction + 1)%4
        
        return answer
                
            
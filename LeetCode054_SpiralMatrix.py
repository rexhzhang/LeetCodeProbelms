"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].


"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        row = len(matrix)
        column = len(matrix[0])

        startRow, endRow, startColumn, endColumn = 0, row - 1, 0, column - 1

        direction = 0
        ans = []
        while startRow <= endRow and startColumn <= endColumn:

            if direction == 0:
                for i in range(startColumn,endColumn+1):
                    ans.append(matrix[startRow][i])
                startRow += 1

            elif direction == 1:
                for i in range(startRow, endRow+1):
                    ans.append(matrix[i][endColumn])
                endColumn -= 1

            elif direction == 2:
                for i in range(endColumn, startColumn-1, -1):
                    ans.append(matrix[endRow][i])
                endRow -= 1

            elif direction == 3:
                for i in range(endRow,startRow-1, -1):
                    ans.append(matrix[i][startColumn])
                startColumn += 1

            direction = (direction + 1) % 4

        return ans


test = Solution()

result = test.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
print(result)
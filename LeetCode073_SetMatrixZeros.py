"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return

        row, column = len(matrix), len(matrix[0])
        row0 = False
        for x in range(column):
            if matrix[0][x] == 0:
                row0 = True
                break # Row[0] contains 0

        for y in range(1, row):
            for x in range(column):
                if matrix[y][x] == 0:
                    matrix[0][x] = 0
                    matrix[y][0] = 0


        for y in range(1, row):
            if matrix[y][0] == 0:
                for x in range(column):
                    matrix[y][x] = 0

        for x in range(column):
            if matrix[0][x] == 0:
                for y in range(row):
                    matrix[y][x] = 0


        if row0 == False:
            return
        else:
            for x in range(column):
                matrix[0][x] = 0

            return

test = Solution()
test.setZeroes()
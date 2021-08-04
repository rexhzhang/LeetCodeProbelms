"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        PascalsTriangle = [[1] * (i + 1) for i in range(numRows)]

        for i in range(numRows):
            for j in range(1, i):
                PascalsTriangle[i][j] = PascalsTriangle[i-1][j-1]+PascalsTriangle[i-1][j]

        return PascalsTriangle


test = Solution()
result = test.generate(5)
print(result)
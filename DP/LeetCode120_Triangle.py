"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

"""
Applying, DP in bottom-up manner we should solve our problem as:
Example:

   3
  7 4
 2 4 6
8 5 9 3

Step 1 :
3 0 0 0
7 4 0 0
2 4 6 0
8 5 9 3

Step 2 :
3  0  0  0
7  4  0  0
10 13 15 0

Step 3 :
3  0  0  0
20 19 0  0

Step 4:
23 0 0 0

output : 23
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # bottom up solution, O(n) extra space

        if triangle is None:
            return print("the input triangle is None!")

        res = triangle[-1]

        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j] + res[j+1]) + triangle[i][j]

        return res[0]
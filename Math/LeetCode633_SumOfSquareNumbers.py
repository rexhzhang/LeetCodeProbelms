"""
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: 3
Output: False
"""
import math


class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c is None or c < 0: return False
        a, b = 0, int(math.sqrt(c))
        while a <= b:
            if a ** 2 + b ** 2 > c:
                b -= 1
            elif a** 2 + b ** 2 < c:
                a += 1

            else:
                return True

        return False

obj = Solution()
print(obj.judgeSquareSum(3))
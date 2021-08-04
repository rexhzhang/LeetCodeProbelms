"""
Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.


Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated

"""


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x is None or x < 0:
            return "Error"
        start, end = 0, x
        while start + 1 < end:
            mid = (start + end) // 2

            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                end = mid
            else:
                start = mid

        if end ** 2 <= x:
            return end
        elif start ** 2 <= x:
            return start

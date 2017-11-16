"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
"""


class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start, end = 0, num
        while start + 1 < end:
            mid = (start + end) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                end = mid
            else:
                start = mid

        if start ** 2 == num:
            return True
        elif end ** 2 == num:
            return True

        return False
"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x is None:
            return print("The input x is None!")
        xStr = str(x)
        length = len(xStr)
        if xStr[0] == "-":
            if int(xStr[length-1:0:-1]) > 2**31:
                return 0
            else:
                return -1* int(xStr[length-1:0:-1])

        else:
            if int(xStr[::-1]) > 2**31:
                return 0
            else:
                return int(xStr[::-1])

    def reverseWithoutCheating(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0

        while x != 0:
            newResult = result * 10 + x % 10
            if (newResult - x % 10)/10 != result:
                return 0
            result = newResult
            x /= 10

        return result
test = Solution()
print(test.reverse(-12313123))
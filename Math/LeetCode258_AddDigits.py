"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

Credits:
"""

"""
Solution:

"""


class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            temp = 0
            while num > 0:
                temp += num % 10
                num /= 10

            num = temp

        return num

    def addDigits2(self, num):
        """
        # using Congruence formula
        100a+10b+c, then (100a+10b+c)%9=(a+99a+b+9b+c)%9=(a+b+c)%9
        :param num: int
        :return: int
        """
        if num == 0:
            return 0
        elif num % 9 != 0:
            return num % 9
        else:
            return 9

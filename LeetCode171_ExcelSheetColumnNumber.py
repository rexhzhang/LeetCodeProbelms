"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
Credits:
"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        for i in range(ord('A'), ord('Z') + 1):
            dict[chr(i)] = i - ord('A') + 1

        """
        dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

        """
        s_reversed = s[::-1]
        ans = 0
        """
        因为是倒着的string AB - > BA所以A位其实是26 ** 1 次方
        """
        for digit, char in enumerate(s_reversed, 0):
            ans = ans + dict[char] * (26 ** digit)

        return ans
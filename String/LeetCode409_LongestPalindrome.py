"""Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that
can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hmap = [0] * 128

        for char in s:
            hmap[ord(char)] += 1

        ans = 0
        single = False
        for num in hmap:
            if num > 0 and num % 2 == 0:
                ans += num

            if num > 0 and num % 2 != 0:
                if num > 1:
                    ans += num-1
                    single = True

                if num == 1:
                    single = True

        if single:
            ans += 1

        return ans
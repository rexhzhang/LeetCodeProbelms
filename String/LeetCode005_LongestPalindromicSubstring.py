"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
"""
"""
# 写一个helper函数，从中间往两头check，需要handle两种情况 1.abba， 2. aba

"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) == 0:
            return ""

        def checkPalindrome(string, start, end):
            while  start >= 0 and end < len(string) and s[start] == s[end]:
                start -= 1
                end += 1

            return s[start + 1:end] # python中start是inclusive，end 是exclusive的

        ans = ""
        for i in range(len(s)):
            # aba
            result = checkPalindrome(s,i,i)
            if len(result) > len(ans):
                ans = result

            # abba
            result = checkPalindrome(s,i,i+1)
            if len(result) > len(ans):
                ans = result

        return ans

test = Solution()
result = test.longestPalindrome("abcbba")
print(result)


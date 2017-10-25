"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""

"""dp[0] means an empty string will have one way to decode, dp[1] means the way to decode a string of size 
1. I then 
check one digit and two digit combination and save the results along the way. In the end, dp[n] will be the end 
result. """

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0

        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1 if s[0] !="0" else 0
        for i in range(2, n+1):
            singleDigit = int(s[i-1:i])
            doubleDigit = int(s[i-2:i])
            if 1 <= singleDigit <= 9:
                dp[i] += dp[i-1]

            if 10 <= doubleDigit <= 26:
                dp[i] += dp[i-2]

        return dp[n]

test = Solution()
print(test.numDecodings("121"))
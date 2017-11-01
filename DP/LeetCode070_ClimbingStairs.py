"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        elif n == 1: return 1
        elif n == 2: return 2

        dp = [0] * (n+1)

        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1]+ dp[i-2]
        return dp[n]

    def climbStairs_O1Space(self, n):
        if n == 0: return 0
        elif n == 1: return 1
        elif n == 2: return 2
        dp = [0, 0]
        dp[0], dp[1] = 1, 2
        for i in range(2,n):
            dp[i%2] = dp[(i-1)%2] + dp[(i-2)%2]

        return dp[(n-1)%2]
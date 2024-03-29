"""You are a professional robber planning to rob houses along a street. Each house has a certain amount of money
stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system
connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police. """


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        if n == 0:
            return 0

        dp = [0, 0]

        dp[0] = 0  # 前0个房子能获得的最大值
        dp[1] = nums[0]  # 前1个房子能获得的最大值

        for i in range(2, n + 1):
            dp[i % 2] = max(dp[(i - 1) % 2], nums[i - 1] + dp[(i - 2) % 2])  # 使用滚动数组优化

        return dp[n % 2]
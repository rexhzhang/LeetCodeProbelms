"""
Given an array nums of n integers, find two integers in nums such that the sum is closest to a given number, target.

Return the difference between the sum of the two integers and the target.

Have you met this question in a real interview? Yes
Example
Given array nums = [-1, 2, 1, -4], and target = 4.

The minimum difference is 1. (4 - (2 + 1) = 1).

Challenge
Do it in O(nlogn) time complexity.
"""


class Solution:
    # @param {int[]} nums an integer array
    # @param {int} target an integer
    # @return {int} the difference between the sum and the target
    def twoSumClosest(self, nums, target):
        # Write your code here

        if not nums or len(nums) < 2:
            return 0

        nums.sort()
        left, right = 0, len(nums) - 1
        diff = float('inf')

        while left < right:
            temp = nums[left] + nums[right]
            if temp > target:
                diff = min(diff, temp - target)
                right -= 1
            else:
                diff = min(diff, target - temp)
                left += 1

        return diff
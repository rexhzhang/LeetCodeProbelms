"""
Given an array of integers, find how many pairs in the array such that their sum is less than or equal to a specific target number. Please return the number of pairs.

Have you met this question in a real interview? Yes
Example
Given nums = [2, 7, 11, 15], target = 24.
Return 5.
2 + 7 < 24
2 + 11 < 24
2 + 15 < 24
7 + 11 < 24
7 + 15 < 25
"""


class Solution:
    # @param nums {int[]} an array of integer
    # @param target {int} an integer
    # @return {int} an integer
    def twoSum5(self, nums, target):
        # 暴力做法：两个loop循环，第二个loop从 i+1到end
        # 这题的关键是排序的数组，因从小到大排序，左是0开始，
        # 第0个数同时又是最小数，如果第0个数+右边都不能小于target，只能right -= 1
        if not nums or len(nums) < 2:
            return 0

        nums.sort()
        left, right = 0, len(nums) - 1
        answer = 0
        while left < right:
            value = nums[left] + nums[right]
            if value > target:
                right -= 1
            else:
                # 中间的pairs都满足
                answer += right - left
                left += 1
        return answer


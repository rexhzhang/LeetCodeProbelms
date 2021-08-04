"""
Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target
number. Please return the number of pairs.

Have you met this question in a real interview? Yes
Example
Given nums = [1,1,2,45,46,46], target = 47
return 2

1 + 46 = 47
2 + 45 = 47
"""


class Solution:
    # @param nums {int[]} an array of integer
    # @param target {int} an integer
    # @return {int} an integer
    def twoSum6(self, nums, target):
        # Write your code here

        if not nums or len(nums) < 2:
            return 0
        left, right = 0, len(nums) - 1
        counter = 0
        nums.sort()

        while left < right:
            value = nums[left] + nums[right]
            if value == target:
                counter += 1
                left += 1
                right -= 1
                # while 要卸载 if 里
                while (left < right) and (nums[left] == nums[left - 1]):
                    left += 1
                while (left < right) and (nums[right] == nums[right + 1]):
                    right -= 1
            elif value > target:
                right -= 1
            else:
                left += 1
        return counter
"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the
non-zero elements.

Notice
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

Given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
"""


class Solution:
    """
    @param: nums: an integer array
    @return:
    """

    def moveZeroes(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return

        slow, fast = 0, 0

        while fast < len(nums):
            while fast < len(nums) and nums[fast] == 0:
                fast += 1
            if fast < len(nums):
                temp = nums[slow]
                nums[slow] = nums[fast]
                nums[fast] = temp
                slow += 1
                fast += 1

        return

"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

 Notice

You may assume no duplicate exists in the array.

Have you met this question in a real interview? Yes
Example
Given [4, 5, 6, 7, 0, 1, 2] return 0
"""


class Solution:
    # @param nums: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return -1
        start, end = 0, len(nums) - 1

        if nums[start] < nums[end]:
            return nums[start]

        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid

        if nums[start] <= nums[end]:
            return nums[start]
        else:
            return nums[end]
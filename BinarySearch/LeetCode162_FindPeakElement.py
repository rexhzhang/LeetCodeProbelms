"""
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
"""


class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return "Invalid Input"

        n = len(nums)
        if n == 1: return 0
        if nums[0] > nums[1]:
            return 0
        elif nums[n - 1] > nums[n - 2]:
            return n - 1

        start, end = 0, n - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid

            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid

        if nums[start] > nums[start - 1] and nums[start] > nums[start + 1]:
            return start
        else:
            return end
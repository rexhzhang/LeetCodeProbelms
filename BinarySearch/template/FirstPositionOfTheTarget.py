"""
For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.

If the target number does not exist in the array, return -1.


Example
If the array is [1, 2, 3, 3, 4, 5, 10], for given target 3, return 2.
"""


class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        # write your code here
        if nums is None or len(nums) == 0 or target is None: return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] == target:
                end = mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid

        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return - 1
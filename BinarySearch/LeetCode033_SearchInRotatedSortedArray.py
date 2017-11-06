"""

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) == 0 or target is None:
            return -1

        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if nums[start] < nums[mid]:  # start, mid, pivot
                if nums[start] <= target and target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:  # start, pivot, mid
                if nums[mid] <= target and target <= nums[end]:
                    start = mid
                else:
                    end = mid

        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        return -1



"""
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""
"""
Solution: 查找两次第一次出现和最后一次出现的位置
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        A = nums
        if not A or len(A) == 0:
            return [-1, -1]

        start, end = 0, len(A) - 1

        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid] < target:
                start = mid
            else:
                end = mid

        if A[start] == target:
            head = start
        elif A[end] == target:
            head = end
        else:
            head = -1

        start, end = 0, len(A) - 1

        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid] <= target:
                start = mid
            else:
                end = mid

        if A[end] == target:
            tail = end
        elif A[start] == target:
            tail = start
        else:
            tail = -1

        return [head, tail]
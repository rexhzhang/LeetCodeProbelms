"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        O(nlog(n)) Time
        O(1) Space
        """
        return sorted(nums)[len(nums)/2]

    def majorityElementII(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        O(n) Time
        O(1) Space
        """
        count = 0; candidate = None

        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]
                count += 1
            elif nums[i] == candidate:
                count += 1
            else:
                count -= 1

        return candidate
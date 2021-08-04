"""
Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
Note: Your solution should run in O(log n) time and O(1) space.
"""
"""
如何利用二分：
看序号和奇偶
"""


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        位运算
        """
        answer = nums[0]
        for i in nums[1:]:
            answer = answer ^ i

        return answer

    def singleNonDuplicate_BinarySearch(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums)-1

        while start + 1 < end:

            mid = (start + end) / 2

            if nums[mid]
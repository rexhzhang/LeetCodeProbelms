"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.sumFromBegining = [nums[i] for i in range(n)]
        for i in range(1, n):
            self.sumFromBegining[i] = self.sumFromBegining[i-1] + self.sumFromBegining[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumFromBegining[j] - self.sumFromBegining[i-1] if i > 0 else self.sumFromBegining[j]

        # 注意减i-1，不是i，面试时走一遍例子

        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # param_1 = obj.sumRange(i,j) obj.sumRange(i,j)
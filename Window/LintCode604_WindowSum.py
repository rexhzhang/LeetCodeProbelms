"""
Given an array of n integer, and a moving window(size k), move the window at each iteration from the start of the array,
find the sum of the element inside the window at each moving.

Example
For array [1,2,7,8,5], moving window size k = 3.
1 + 2 + 7 = 10
2 + 7 + 8 = 17
7 + 8 + 5 = 20
return [10,17,20]
"""


class Solution:
    # @param nums {int[]} a list of integers
    # @param k {int} size of window
    # @return {int[]} the sum of element inside the window at each moving
    def winSum(self, nums, k):
        if nums is None or len(nums) == 0 or k <= 0: return []

        windowSum = 0
        resultList = []
        for i in range(k):
            windowSum += nums[i]
        resultList.append(windowSum)

        for i in range(k, len(nums)):
            windowSum -= nums[i - k]
            windowSum += nums[i]

            resultList.append(windowSum)

        return resultList

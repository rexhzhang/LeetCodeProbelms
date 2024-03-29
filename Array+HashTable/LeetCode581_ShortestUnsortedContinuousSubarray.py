"""Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending
order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxNum, minNum = nums[0], nums[n - 1]
        start, end = -1, -2
        for i in range(n):
            maxNum = max(maxNum, nums[i])
            minNum = min(minNum, nums[n - 1 - i])
            if nums[i] < maxNum: end = i
            if nums[n - 1 - i] > minNum: start = n - 1 - i

        return end + 1 - start
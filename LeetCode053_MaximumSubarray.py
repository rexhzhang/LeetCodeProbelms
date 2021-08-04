"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums is None:
            return 0

        currentSum = nums[0]
        MaxSum = currentSum

        for num in nums[1:]:
            currentSum = max(num, num+currentSum)
            MaxSum = max(MaxSum, currentSum)

        return MaxSum



test = Solution()
result = test.maxSubArray([4,-1,2,1])
print(result)
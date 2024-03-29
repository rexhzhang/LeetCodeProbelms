"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""


class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return []
        count, left, right, end = {}, {}, {}, len(nums) - 1
        for i in range(len(nums)):
            if nums[i] not in left:
                left[nums[i]] = i
            if nums[end - i] not in right:
                right[nums[end-i]] = end - i
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
        degreeOfArray = max(count.values())
        minLength = len(nums)
        for key in count:
            if count[key] == degreeOfArray:
                minLength = min(minLength, right[key] - left[key] + 1)
        return  minLength

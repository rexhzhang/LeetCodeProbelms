"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""


class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        """
        O(n^3) Time, O(1) space
        2 for loops uses O(n^2) Time, and worst case O(n) to calculate the sum 
        """
        if nums is None or k is None or len(nums) == 0: return 0
        answer = 0
        for start in range(len(nums)):
            for end in range(start, len(nums)):
                if sum(nums[start:end+1]) == k:
                    answer += 1
                # elif sum(nums[start:end+1]) > k:      # this is invalid as there can be negative elements in array
                #     break
        return answer

    def subarraySum2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        O(n^2) Time, O(1) space
        """
        if nums is None or k is None or len(nums) == 0: return 0
        answer = 0
        for start in range(len(nums)):
            summ = 0
            for end in range(start, len(nums)):
                summ += nums[end]
                if summ == k:
                    answer += 1

        return answer

    def subarraySum3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        O(n) Time, O(n) space
        """
        if nums is None or k is None or len(nums) == 0: return 0
        answer = 0
        sum = 0
        hashMap = {}
        hashMap[0] = 1 # <SUM(0,i), # of Occurance of SUM(0,i)>
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in hashMap:
                answer += hashMap.get(sum-k)

            if sum in hashMap:
                hashMap[sum] += 1
            else:
                hashMap[sum] = 1

        return answer
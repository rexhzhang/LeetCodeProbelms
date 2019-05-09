"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        preMax = preMin = globalMax = nums[0]
        
        for n in nums[1:]:
            if n > 0:
                curMax = max(n, n * preMax)
                curMin = min(n, n * preMin)
            
            else:
                curMax = max(n, n * preMin)
                curMin = min(n, n * preMax)
            
            globalMax = max(globalMax, curMax)
            preMax = curMax
            preMin = curMin
        
        return globalMax
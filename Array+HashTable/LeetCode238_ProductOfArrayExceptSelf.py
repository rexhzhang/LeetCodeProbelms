"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 乘法分成两轮，先prefix product从左往右，再prefix product从右向左，正好没有乘自己
        res = [1] * len(nums)
        
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        
        prefixProductFromRight = 1
        
        for i in range(len(nums)-1, -1, -1):
            res[i] *= prefixProductFromRight
            prefixProductFromRight *= nums[i]
        
        return res
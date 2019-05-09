"""
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:

Input: nums = [-2,0,1,3], and target = 2
Output: 2 
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
Follow up: Could you solve it in O(n2) runtime?
"""
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # This question allows duplicate.
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n-2):
            left = i + 1
            right = n - 1
            
            while left < right:
                if nums[i] + nums[left] + nums[right] < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1
            
        
        return count
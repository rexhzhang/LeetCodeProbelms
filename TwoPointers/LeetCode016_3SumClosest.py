"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) < 3: return
        
        nums.sort()
        best_sum = None
        for i in range(len(nums)):

            left, right = i+1, len(nums)-1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if abs(current_sum-target) < abs(best_sum - target):
                    best_sum = current_sum

                if current_sum <= target:
                    left += 1
                
                else:
                    right -= 1
            
        return best_sum

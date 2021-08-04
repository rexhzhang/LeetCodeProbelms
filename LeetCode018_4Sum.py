"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        
        answer = []
        # 排序
        nums.sort()
        
        for i in range(len(nums)-3):
            # 去重
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, len(nums)-2):
                # 去重
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                left = j + 1
                right = len(nums) -1
                
                while left < right:
                    summ = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if summ == target:
                        answer.append([nums[i], nums[j], nums[left], nums[right]])
                        # 去重
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # 去重
                        while left < right and nums[right-1] == nums[right]:
                            right -= 1
                        left += 1
                        right -= 1
                    
                    elif summ > target:
                        right -=1
                    else:
                        left += 1
            
        return answer
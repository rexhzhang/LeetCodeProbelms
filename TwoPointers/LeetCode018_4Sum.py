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
        if not nums or len(nums) < 4:
            return []
        
        nums.sort()
        answer = []
        
        for i in range(len(nums)-3):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, len(nums)-2):
                
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                    
                start, end = j + 1, len(nums)-1

                while start < end:

                    if (nums[i] + nums[j] + nums[start] + nums[end]) == target:
                        answer.append([nums[i], nums[j], nums[start], nums[end]])

                        while start < end and nums[start] == nums[start+1]:
                            start += 1

                        while start < end and nums[end] == nums[end-1]:
                            end -= 1

                        start += 1
                        end -=1

                    elif nums[i] + nums[j] + nums[start] + nums[end] < target:
                        start += 1
                        
                    else:
                        end -= 1
            
        return answer
                        
                        
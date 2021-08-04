"""
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""
"""
Solution: 查找两次第一次出现和最后一次出现的位置
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        ans = [-1, -1]
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            
            mid = (start + end) // 2
            
            if nums[mid]< target:
                start = mid
            
            else:
                end = mid
    
        if nums[start] == target:
            ans[0] = start
        elif nums[end] == target:
            ans[0] = end
        

        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            
            mid = (start + end) // 2
            
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        
        if nums[end] == target:
            ans[1] = end
        elif nums[start] == target:
            ans[1] = start
        
        return ans
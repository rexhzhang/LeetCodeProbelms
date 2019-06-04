"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return
        start, end = 0, len(nums) - 1
        
        if nums[start] <nums[end]: return nums[start]
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid
        
        if nums[start] > nums[end]:
            return nums[end]
        else:
            return nums[start]
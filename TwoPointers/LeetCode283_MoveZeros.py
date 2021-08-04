"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Swap, 不保证写次数最小
        if not nums:
            return
        
        l, r = 0, 0

        while r < len(nums):

            if nums[r] != 0:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
            
            # 如果右指针指向的数是0，越过
            r += 1
    
        return




    def moveZerosII(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 这个版本可以保证最小的“写”次数。

        if not nums: return
        
        left, right = 0, 0

        # 在原数组建立新的数组
        while right < len(nums):

            if nums[right] != 0:
                if left != right:
                    nums[left] = nums[right]
                left += 1
            
            right += 1
        
        # left 指针之后都为0
        while left < len(nums):
            if nums[left] != 0:
                nums[left] = 0
            left += 1
        

        return
"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""

#方法一： O(2n), O(1) 第一遍记住个数，第二遍修改
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        memory = [0,0,0]
        for n in nums:
            if n == 0:
                memory[0] += 1
            elif n == 1:
                memory[1] += 1
            elif n == 2:
                memory[2] += 1
            else:
                print("Unexpceted Value Error! ")
                break
        
        for i in range(len(nums)):
            if memory[0] > 0:
                nums[i] = 0
                memory[0] -= 1
            elif memory[1] > 0:
                nums[i] = 1
                memory[1] -= 1
            else:
                
                nums[i] = 2
                memory[2] -= 1


    #方法二：O(n), O(1)

    def sortColorsII(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left, index, right = 0,0,len(nums)-1
        # left表示左起第一个不为0的数
        while index <= right:
            
            if nums[index] == 0:
                nums[index], nums[left] = nums[left], nums[index]
                left += 1
                index += 1
            
            elif nums[index] == 1:
                index += 1
            
            else:
                nums[index], nums[right] = nums[right], nums[index]
                right -= 1
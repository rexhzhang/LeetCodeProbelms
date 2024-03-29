"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
"""
xor(^): 任何数xor本身 = 0
a = 10,  00001010 
b = 20,  00010100

a^a : 00001010
      00001010
      00000000
      
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result = result ^ num

        return result
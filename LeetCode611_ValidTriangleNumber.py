"""
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles 
if we take them as side lengths of a triangle.
Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].
"""
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        if n < 3:
            return 0
        
        nums.sort()
        count = 0
        for k in range(n-1, 1, -1):
            start, end = 0, k - 1
            
            while start < end:
                if nums[start] + nums[end] > nums[k]:
                    count += end - start
                    end -= 1
                
                else:
                    start += 1
            
        
        return count
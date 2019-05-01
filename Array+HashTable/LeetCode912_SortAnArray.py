"""
Given an array of integers nums, sort the array in ascending order.

 

Example 1:

Input: [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

Note:

1 <= A.length <= 10000
-50000 <= A[i] <= 50000
"""

import random
class Solution:
    
    def sortArray(self, nums: List[int]) -> List[int]:
    """
    Runtime: O(nlogn) expected, O(n^2) worst case.
    With a proper choice of pivot (using the median of medians algorithm), the runtime can be reduced to strict O(nlogn).
    Space: O(n) expected, O(n^2) worst case
    """    
        if len(nums) <= 1:
            return nums
        
        pivot =  random.choice(nums)
        
        lt = [v for v in nums if v < pivot]
        eq = [v for v in nums if v == pivot]
        gt = [v for v in nums if v > pivot]
        
        return self.sortArray(lt) + eq + self.sortArray(gt)
    
        
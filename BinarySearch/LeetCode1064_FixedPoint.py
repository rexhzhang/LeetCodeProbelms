"""
Given an array A of distinct integers sorted in ascending order, return the smallest index i that satisfies A[i] == i.  Return -1 if no such i exists.

 

Example 1:

Input: [-10,-5,0,3,7]
Output: 3
Explanation: 
For the given array, A[0] = -10, A[1] = -5, A[2] = 0, A[3] = 3, thus the output is 3.
Example 2:

Input: [0,2,5,8,17]
Output: 0
Explanation: 
A[0] = 0, thus the output is 0.
Example 3:

Input: [-10,-5,3,4,7,9]
Output: -1
Explanation: 
There is no such i that A[i] = i, thus the output is -1.
 

Note:

1 <= A.length < 10^4
-10^9 <= A[i] <= 10^9
"""
class Solution(object):
    def fixedPoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        if not A: return -1
        
        start, end = 0, len(A)-1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if mid <= A[mid]:
                end = mid
            else:
                start = mid
        
        if A[start] == start:
            return start
        
        if A[end] == end:
            return end
        
        return -1




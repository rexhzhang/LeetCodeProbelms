"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

1
2
3
4
5
6
7
8
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note: 
You may assume k is always valid, ie: 1 ≤ k ≤ input array’s size for non-empty array.

Follow up:
Could you solve it in linear time?
"""

from collections import deque

class MaxQueue:
    def __init__(self):
        self._q = deque()
    
    def push(self, e):
        while self._q and e > self._q[-1]: self._q.pop()
    
    def pop(self):
        self._q.popleft()
    
    def max(self):
        return self._q[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        q = MaxQueue()
        result = []
        for i in range(len(nums)):
            q.push(nums[i])
            if i >= k-1:
                result.append(q.max())
                if nums[i - k + 1] == q.max(): q.pop()
        return result


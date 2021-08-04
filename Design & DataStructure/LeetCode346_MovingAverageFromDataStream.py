"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""

from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.current_size = 0
        self.q = deque()
        self.current_sum = 0

    def next(self, val: int) -> float:
        
        self.q.append(val)
        self.current_size += 1
        self.current_sum += val
        
        if self.current_size <= self.size:
            return self.current_sum/self.current_size
        
        else:
            self.current_sum -= self.q.popleft()
            
            return self.current_sum/self.size

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
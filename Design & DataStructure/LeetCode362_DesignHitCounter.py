"""
Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

Example:

HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301); 
Follow up:
What if the number of hits per second could be very large? Does your design scale?
"""
from collections import deque

# 方法一： O(1) hit, O(s) getHits
# O(s) space
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 5 mins = 300 seconds
        self.hits = [0] * 300
        self.time = [0] * 300


    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        index = timestamp % 300
        
        if self.time[index] != timestamp:
            self.time[index] = timestamp
            self.hits[index] = 1
        else:
            self.hits[index] += 1
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        total_hits = 0
        for i in range(300):
            if timestamp - self.time[i] < 300:
                total_hits += self.hits[i]
        return total_hits 

# 方法2: Deque
# O(1) hit, O(s) getHits
# O(s) space
class HitCounter2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.total_hits = 0
        self.timeline = deque() 

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if self.timeline and self.timeline[-1][0] == timestamp:
            self.timeline[-1][1] += 1
            self.total_hits += 1
        
        else:
            self.timeline.append([timestamp, 1])
            self.total_hits += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        
        while self.timeline and self.timeline[0][0] <= timestamp - 300:
            hit = self.timeline.popleft()
            self.timeline -= hit[1]
        
        return self.total_hits


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
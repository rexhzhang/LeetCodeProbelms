"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        timeline = []
        
        for start, end in intervals:
            timeline.append([start,1])
            timeline.append([end, -1])
        
        count = 0
        max_count = 0
        
        for time in sorted(timeline):
            count += time[1]
            max_count = max(count, max_count)
        
        return max_count
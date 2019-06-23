"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
"""

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        timeline = []
        for start, end in intervals:
            timeline.append([start, 1])
            timeline.append([end,-1])
        
        count = 0
        max_count = 0
        for meeting in sorted(timeline):
            count += meeting[1]
            max_count = max(count, max_count)
        
        return max_count <= 1
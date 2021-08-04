"""
Given an interval list which are flying and landing time of the flight. How many airplanes are on the sky at most?

 Notice
If landing and flying happens at the same time, we consider landing should happen at first.

For interval list

[
  [1,10],
  [2,3],
  [5,8],
  [4,7]
]
Return 3
"""

from operator import itemgetter
# Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


# def comperator(x, y):
#     if x[0] != y[0]:
#         return x[0] - y[0]
#     return x[1] - y[1]


class Solution:
    # @param airplanes, a list of Interval
    # @return an integer
    def countOfAirplanes(self, airplanes):
        # write your code here

        timeline = []

        for airplane in airplanes:
            timeline.append((airplane[0], 1))
            timeline.append((airplane[1], -1))

        timeline = sorted(timeline, key=itemgetter(0,1))

        counter = 0
        most = 0

        for u, v in timeline:  # 此处u要不是起飞，要不是落地，并且已经排序
            counter += v
            most = max(counter, most)

        return most

test = Solution()
testCase = [[1,10],[2,3],[5,8],[4,7]]
result = test.countOfAirplanes(testCase)
print(result)
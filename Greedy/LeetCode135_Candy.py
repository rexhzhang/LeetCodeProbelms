"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
"""


class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        """
        ratings     1 2 3 4 2 1 1
        forward     1 2 3 4 1 1 1
        backward    1 2 3 4 2 1 1
        """
        if len(ratings) == 0 or ratings is None: return 0
        candys = [1] * len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                candys[i] = candys[i-1]+1

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candys[i] = max(candys[i+1]+1, candys[i])

        # print(candys)

        return sum(candys)

test = Solution()
test.candy([1,2,3,4,2,1,1])
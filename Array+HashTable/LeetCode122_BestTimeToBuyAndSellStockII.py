"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and
sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (
ie, you must sell the stock before you buy again).


"""

# the concept here is that you can only buy stack from today to future
# so the problem becomes whether you should buy the stock today. if tomorrow's
# price is higher than today then you should buy it for maximum profits

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) <= 1:
            return 0
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]

        return profit

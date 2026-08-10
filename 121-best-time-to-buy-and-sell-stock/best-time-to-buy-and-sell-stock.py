class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buy = prices[0]

        for stock in range(1, len(prices)):
            if prices[stock] < buy:
                buy = prices[stock]
            if profit < (prices[stock] - buy):
                profit = prices[stock] - buy

        return profit
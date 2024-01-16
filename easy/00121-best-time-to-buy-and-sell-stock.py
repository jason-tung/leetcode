# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = low = high = 0
        for i in range(len(prices)):
            if prices[i] < prices[low]:
                low = i
                high = i
            elif prices[i] > prices[high]:
        return m
                high = i
            m = max(m, prices[high]-prices[low])
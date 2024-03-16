# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m,low = 0,float('inf')
        for k in prices:
            if k < low:
                low = k
            else:
                m = max(m, k - low)
        return m
#https://leetcode.com/problems/climbing-stairs/description/
class Solution:
    # opt n = opt (n-1) + opt(n-2)
    def climbStairs(self, n: int) -> int:
        low,high=0,1
        for i in range(n):
            low, high = high, low + high
        # runs sloewr than caching with list but ok
        return high
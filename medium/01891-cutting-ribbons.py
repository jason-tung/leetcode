# https://leetcode.com/problems/cutting-ribbons/
class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        mx = max(ribbons)
        l,r = max(1, mx//k), min(mx, sum(ribbons)//k)
        while l <= r:
            t = 0
            m = (l + r)//2
            for i in ribbons:
                t += i // m
            if t < k:
                r = m - 1
            else:
                l = m + 1
        return r
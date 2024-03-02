# https://leetcode.com/problems/powx-n/
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        sign = n < 0
        if sign:
            n = -n
        res = self.myPow(x, n // 2)
        res *= res
        if n % 2:
            res *= x
        return 1/res if sign else res
# x ^ n = x ^ n//2 * x ^ n//2 * x if n%2
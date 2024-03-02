# https://leetcode.com/problems/powx-n/
# small opt
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x*x, n //2)
        return self.myPow(x*x, n/2)
# x ^ n = x ^ n//2 * x ^ n//2 * x if n%2
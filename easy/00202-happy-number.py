# https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        s = {}
        while n != 1:
            m = 0
            while n:
                m += (n % 10)**2
                n //= 10
            n = m
            if n in s:
                return False
            s[n] = True
        # can do a better job with cycle detection by using
        # floyd algo
        return True
# https://leetcode.com/problems/happy-number/
        while n != 1:
            m = 0
            while n:
                m += (n % 10)**2
                n //= 10
            n = m
            s[n] = True
        s = {}
    def isHappy(self, n: int) -> bool:
            if n in s:
                return False
        return True
class Solution:
# https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        sol = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        while x:
            ns = 10 * sol + x % 10
            # py doesnt let you strictly cast to 32bit int
            if ns > 2**31 -1 or ns < -2**31 or (ns - x % 10) / 10 != sol:
                return 0
            sol = ns
            x //= 10
        return sign * sol
            
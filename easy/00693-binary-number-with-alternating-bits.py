# https://leetcode.com/problems/binary-number-with-alternating-bits/
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = (n&1)^1
        while n:
            if b == n&1:
                return False
            b = n&1
            n >>= 1
        return True
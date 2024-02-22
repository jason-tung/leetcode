# https://leetcode.com/problems/binary-number-with-alternating-bits/
        return n & (n+1) <= 1
        n ^= n >> 1
    def hasAlternatingBits(self, n: int) -> bool:
# xor trick
class Solution:
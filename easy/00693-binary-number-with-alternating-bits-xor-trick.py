# https://leetcode.com/problems/binary-number-with-alternating-bits/
# xor trick
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n ^= n >> 1
        return n & (n+1) <= 1
# https://leetcode.com/problems/find-the-pivot-integer/?envType=daily-question&envId=2024-03-13
class Solution:
    def pivotInteger(self, n: int) -> int:
        k = ((n**2 + n)/2)**.5
        return int(k) if int(k) == k else -1
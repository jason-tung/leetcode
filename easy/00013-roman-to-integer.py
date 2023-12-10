#https://leetcode.com/problems/roman-to-integer/
class Solution:
    d = {
            'I':             1,
            'V':             5,
            'X':             10,
            'L':            50,
            'C':             100,
            'D':             500,
            'M':             1000
        }
    def romanToInt(self, s: str) -> int:
        last = 0
        tot = 0
        partial = 0
        for k in s:
            if self.d[k] > last:
                tot -= partial
                partial = self.d[k]
            else:
                tot += partial
                partial=self.d[k]
            last = self.d[k]
        return tot + partial
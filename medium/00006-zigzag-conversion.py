# https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ret = [[] for _ in range(numRows)]
        ins = 0
        incr = 1
        for i in range(len(s)):
            ret[ins].append(s[i])
            ins += incr
            if ins == 0 or ins == numRows - 1:
                incr *= -1
        if numRows == 1:
            return s
        return "".join(y for x in ret for y in x)
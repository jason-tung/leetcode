#https://leetcode.com/problems/add-binary/description/
                t += 1
            if p2 >= 0 and b[p2] == '1':
                t += 1
            co = t >> 1
            out = str(t & 1) + out
        if co:
            return "1"+out
        return out
            if p1 >= 0 and a[p1] == '1':
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        co, out = 0, ""
        max_iter = max(len(a), len(b))
        for i in range(max_iter):
            p1 = len(a) - i - 1
            p2 = len(b) - i - 1
            t = co
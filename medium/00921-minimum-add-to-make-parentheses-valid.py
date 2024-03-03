# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        g,b = 0, 0
        for k in s:
            if k == "(":
                g+=1
            elif g > 0:
                g -= 1
            else:
                b += 1
        return g + b
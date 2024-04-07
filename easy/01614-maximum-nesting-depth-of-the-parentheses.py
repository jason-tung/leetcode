# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/?envType=daily-question&envId=2024-04-04
class Solution:
    def maxDepth(self, s: str) -> int:
        counter = m = 0
        for k in s:
            if k == "(":
                counter += 1
            elif k == ")":
                counter -= 1
            m = max(m, counter)
        return m
        
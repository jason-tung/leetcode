# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s2 = []
        for i in range(len(s)):
            char = s[i]
            if char == "(":
                stack.append(i)
            elif char == ")":
                if len(stack) == 0:
                    s2.append(i)
                else:
                    stack.pop()
        ret = ''
        i, p1, p2 = 0, 0, 0
        while i < len(s):
            if p1 < len(stack) and i == stack[p1]:
                p1 += 1
            elif p2 < len(s2) and i == s2[p2]:
                p2 += 1
            else:
                ret += s[i]
            i += 1
        return ret
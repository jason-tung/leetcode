# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# str to list
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
        for i in range(len(s)):
            char = s[i]
            if char == "(":
                stack.append(i)
            elif char == ")":
                if len(stack) == 0:
                    s[i] = ''
                else:
                    stack.pop()
        while stack:
            s[stack.pop()] = ''
        return ''.join(s)
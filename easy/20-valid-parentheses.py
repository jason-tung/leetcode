#https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            "(":")",
            "{":"}",
            "[":"]",
        }
        for c in s:
            if c in d:
                stack.append(c)
            else:
                if len(stack) == 0 or d[stack.pop()] != c:
                    return False
        return len(stack) == 0
# https://leetcode.com/problems/make-the-string-great/?envType=daily-question&envId=2024-04-05
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for k in range(len(s)):
            if len(stack) > 0:
                if s[k].lower() == stack[-1].lower() and s[k] != stack[-1]:
                    stack.pop()
                else:
                    stack.append(s[k])
            else:
                stack.append(s[k])
        return  ''.join(stack)
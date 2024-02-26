# https://leetcode.com/problems/add-strings/
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        [shorter, longer] = [num1,num2] if len(num1) <= len(num2) else [num2,num1]
        i, c = -1, 0
        output = deque()
        while i >= -len(shorter):
            res = int(shorter[i]) + int(longer[i]) + c
            output.appendleft(str(res%10))
            c = res // 10
            i -= 1
        while i >= -len(longer):
            res = int(longer[i]) + c
            output.appendleft(str(res%10))
            c = res // 10
            i -= 1
        if c:
            output.appendleft(str(c))
        return ''.join(output)
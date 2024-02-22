# https://leetcode.com/problems/baseball-game/
            if x == 'C':
            elif x == '+':
                stack.append(stack[-1] + stack[-2])
        for x in operations:
            elif x == 'D':
                stack.append(stack[-1]*2)
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
                stack.pop()
            else:
                stack.append(int(x))
        return sum(stack)
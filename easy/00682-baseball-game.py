# https://leetcode.com/problems/baseball-game/
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for x in operations:
            if x.isdigit() or x[1:].isdigit():
                stack.append(int(x))
            elif x == '+':
                stack.append(stack[-1] + stack[-2])
            elif x == 'D':
                stack.append(stack[-1]*2)
            else:
                stack.pop()
        return sum(stack)
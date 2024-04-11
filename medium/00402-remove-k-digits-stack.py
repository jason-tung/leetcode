# https://leetcode.com/problems/remove-k-digits/?envType=daily-question&envId=2024-04-11
# stack
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"
        if k == 0:
            return num
        stack = []
        for n in num:
            while k > 0 and stack and n < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(n)
        while k and stack:
            stack.pop()
            k -= 1
        i = 0
        while i < len(stack) and stack and stack[i] == "0":
            stack[i] = ""
            i += 1
        res = ''.join(stack) 
        return res if res else "0"
            
        
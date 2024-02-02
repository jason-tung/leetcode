# https://leetcode.com/problems/basic-calculator-ii/
# stack
def execute(a,b,op):
    if op == "*":
        return str(int(a) * int(b))
    elif op == "/":
        return str(math.trunc(int(a) / int(b)))
    else:
        raise Exception(f'unexpected case {a},{b},{op}')
class Solution:
    def calculate(self, s: str) -> int:
        op, num, stack = "+", "0", []
        for i in range(len(s)):
            c = s[i]
            if c != " " or i == len(s) - 1:
                if c.isdigit():
                    num+=c
                if not c.isdigit() or i == len(s) - 1:
                    if op == "*" or op == "/":
                        past = stack.pop()
                        stack.append(int(execute(past,num, op)))
                    else:
                        stack.append(int(f'{op}{num}'))
                    num = "0"
                    op = c
        return sum(stack)
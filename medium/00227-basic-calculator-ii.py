# https://leetcode.com/problems/basic-calculator-ii/
# 1 + 2 + 3 * 4 * 5 + 6
# two pass solution
def execute(a,b,op):
    if op == "+":
        return str(int(a) + int(b))
    elif op == "-":
        return str(int(a) - int(b))
    elif op == "*":
        return str(int(a) * int(b))
    elif op == "/":
        return str(int(a) // int(b))
    elif op == None:
        return b
    else:
        raise Exception(f'unexpected case {a},{b},{op}')
class Solution:
    def calculate(self, s: str) -> int:
        cur_op, cur_num, last_num = None, "0", "0"
        s = s.replace(" ",  "")
        cachednum, cachedop = "0", None
        for i in range(len(s)):
            c = s[i]
            # print(f'{c};{cur_op},{last_num},{cur_num}')
            if c.isdigit():
                cur_num+=c
                # if it's the end always execute 
                if i == len(s) - 1:
                    sol = execute(last_num, cur_num, cur_op)
                    if not cachedop:
                        return int(sol)
                    return int(execute(cachednum, sol,cachedop))
            else:
                # if c is * then suspend the previous addition until c is not - or =
                if c == "*" or c == "/":
                    if cur_op == "+" or cur_op == "-":
                        # print(f"caching op {cur_op},{last_num}")
                        cachedop = cur_op
                        cachednum = last_num
                    elif cur_op:
                        cur_num = execute(last_num, cur_num, cur_op)
                # if c is + then execute the last store addition if it exists
                if c == "+" or c == "-":
                    # print(f'executing {cur_op},{last_num},{cur_num}')
                    cur_num = execute(last_num, cur_num, cur_op)
                    if cachedop == "+" or cachedop == "-":
                        # print(f'executing cached op {cachedop},{cachednum}')
                        last_num = cachednum
                        cur_op = cachedop
                        cachedop = None
                        cur_num = execute(last_num, cur_num, cur_op)
                last_num = cur_num
                cur_num = "0"
                cur_op = c
            # print(f'ENDLOOP;{c};{cur_op},{last_num},{cur_num}')
            
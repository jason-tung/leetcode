# https://leetcode.com/problems/basic-calculator/
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        opstack = []
        ctotstack = []
        ctot = 0
        num = "0"
        lastop = "+"
        for i in range(len(s)):
            c = s[i]
            if c == "+" or c == "-":
                lastop = c
            elif c == "(":
                ctotstack.append(ctot)
                opstack.append(lastop)
                ctot = 0
                lastop = "+"
            # pop it off and continue execution
            elif c == ")":
                lastop = opstack.pop()
                tempctot = ctotstack.pop()
                ctot = tempctot + ctot if lastop == "+" else tempctot - ctot
            else:
                num += c
                # look-ahead to flush. can also put this into ")" and op logic
                if i == len(s) - 1 or s[i+1] == "+" or s[i+1] == "-" or s[i+1] == ")":
                    ctot += int(num) if lastop == "+" else -int(num)
                    num = "0"
        return ctot
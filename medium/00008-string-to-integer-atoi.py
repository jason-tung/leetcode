# https://leetcode.com/problems/string-to-integer-atoi/
class Solution:
    def myAtoi(self, s: str) -> int:
        while len(s) and s[0] == " ":
            s = s[1:]
        if len(s) == 0:
            return 0 
        sign = -1 if s[0] == "-" else 1
        if s[0] == "+" or s[0] == "-":
            s = s[1:]
        ret = 0
        i = 0
        while i < len(s) and s[i].isdigit():
            ret *= 10
            ret += int(s[i])
            if sign == 1 and ret >= 2**31-1:
                return 2**31-1
            elif sign == -1 and ret >= 2**31:
                return -2**31
            i += 1
        return sign * ret
                
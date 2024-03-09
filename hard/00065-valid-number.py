# https://leetcode.com/problems/valid-number/
signs = set(['+', '-'])
e = set(['e', 'E'])
class Solution:
    def isNumber(self, s: str) -> bool:
        i = len(s)
        for j in range(len(s)):
            if s[j] in e:
                if i != len(s):
                    return False
                i = j
        if i != len(s):
            return isDecimal(s, 0, i) and isInteger(s,i + 1, len(s))
        return isDecimal(s, 0, i)
def isDecimal(s,a,b):
    digits = 0
    dots = 0
    for i in range(a,b):
        if i == a:
            if s[i].isdigit():
                digits += 1
            elif s[i] == ".":
                dots += 1
            elif s[i] not in signs and not s[i].isdigit():
                return False
        elif s[i] == ".":
            dots += 1
        elif s[i].isdigit():
            digits += 1
        else:
            return False
        if dots > 1:
            return False
    return digits > 0
def isInteger(s, a, b):
    digits = 0
    for i in range(a,b):
        if i == a:
            if s[i].isdigit():
                digits += 1
            elif s[i] not in signs and not s[i].isdigit():
                return False
        elif s[i].isdigit():
            digits += 1
        else:
            return False
    return digits > 0
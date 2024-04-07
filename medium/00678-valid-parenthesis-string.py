# https://leetcode.com/problems/valid-parenthesis-string/?envType=daily-question&envId=2024-04-07
class Solution:
    def checkValidString(self, s: str) -> bool:
        good = []
        counter = []
        for i in range(len(s)):
            k = s[i]
            if k == "(":
                counter.append(i)
            elif k == ")":
                if counter:
                    counter.pop()
                elif good:
                    good.pop()
                else:
                    return False
            else:
                good.append(i)
        if len(counter) > len(good):
            return False
        for i in range(-1, -len(counter) - 1, -1):
            if counter[i] > good[i]:
                return False
        return True
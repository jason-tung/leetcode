# https://leetcode.com/problems/isomorphic-strings/
        d = {}
        codomain = set()
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = t[i]
            elif d[s[i]] != t[i]:
                    return False
                if t[i] in codomain:
            codomain.add(t[i])
                    return False
# using definition of bijection
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
            # surjection
            # injection
        return len(s) == len(t)
# https://leetcode.com/problems/isomorphic-strings/
        if c not in d:
            d[c] = len(d)
class Solution:
        l.append(d[c])
    return l
def eq(a,b):
    return len(a) == len(b) and all([a[i] == b[i] for i in range(len(a))])
    def isIsomorphic(self, s: str, t: str) -> bool:
        return eq(toIdentity(s),toIdentity(t))
def toIdentity(s):
    l = []
    d = {}
    for c in s:
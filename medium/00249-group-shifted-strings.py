# https://leetcode.com/problems/group-shifted-strings/
def toRepresentation(s):
    rep = []
    prev = ord(s[0])
    for char in s:
        o = ord(char)
        rep.append((o - prev)%26)
        prev = o
    return tuple(rep)
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        d = {}
        for s in strings:
            rep = toRepresentation(s)
            if rep not in d:
                d[rep] = [s]
            else:
                d[rep].append(s)
        return d.values()
        
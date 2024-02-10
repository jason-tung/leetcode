# https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        l = [0]*26
        c = 0
        for i in range(len(s)):
            i1 = ord(s[i]) - ord('a')
            i2 = ord(t[i]) - ord('a')
            # detect state change in loop instead of doing another loop on ary
            o1,o2 = l[i1],l[i2]
            l[i1] += 1
            l[i2] -= 1
            if o1== 0 and l[i1] != 0:
                c += 1
            elif o1 != 0 and l[i1] == 0:
                c -= 1
            if o2 == 0 and l[i2] != 0:
                c += 1
            elif o2 != 0 and l[i2] == 0:
                c -= 1 
        return c == 0